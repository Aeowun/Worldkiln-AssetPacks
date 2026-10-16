#!/usr/bin/env python3
"""Publish a validated replacement asset catalogue; never mutate historical releases.

Usage: python scripts/publish_kenney_trio.py [--publish]
Dry run validates official archives/checksums without creating a release.
Requires GitHub CLI authenticated to Aeowun to publish.
"""
import argparse
import copy
import hashlib
import io
import json
import re
import subprocess
import sys
import tempfile
import zipfile
from pathlib import Path

REPO = "Aeowun/Worldkiln-AssetPacks"
SOURCE_TAG = "asset-packs-v1.1.0"
BASE_TAG = "asset-packs-v1.5.0"
NEW_TAG = "asset-packs-v1.6.0"
NEW_ID = "kenney-characters-trio"
NEW_ZIP = NEW_ID + "-1.0.0.zip"
SOURCE_IDS = ("character-a", "character-b", "character-c")
RETIRED = {"little-elf-animated", "kenney-blocky-characters"}


def gh(*args):
    process = subprocess.run(["gh", *args], capture_output=True, text=True)
    if process.returncode:
        raise RuntimeError(f"gh {' '.join(args)}: {process.stderr.strip() or process.stdout.strip()}")
    return process.stdout


def release(tag):
    process = subprocess.run(["gh", "api", f"repos/{REPO}/releases/tags/{tag}"],
                             capture_output=True, text=True)
    return json.loads(process.stdout) if process.returncode == 0 else None


def manifests(tag, workspace):
    folder = workspace / tag
    folder.mkdir()
    gh("release", "download", tag, "--repo", REPO, "--dir", str(folder),
       "--pattern", "assets-manifest*.json")
    primary = json.loads((folder / "assets-manifest.json").read_text(encoding="utf-8"))
    if primary.get("schema") != 1 or not isinstance(primary.get("packs"), list):
        raise ValueError(f"Unsupported catalogue schema at {tag}")
    path_v2 = folder / "assets-manifest-v2.json"
    v2 = json.loads(path_v2.read_text(encoding="utf-8")) if path_v2.is_file() else None
    return primary, v2


def sources(catalog, workspace):
    folder = workspace / "original-packs"
    folder.mkdir()
    selected = []
    for pack_id in SOURCE_IDS:
        pack = next((p for p in catalog["packs"] if p["id"] == pack_id), None)
        if not pack or pack.get("dependencies") or pack.get("materials"):
            raise ValueError(f"Missing/unsupported source pack {pack_id}")
        if pack["tag"] != SOURCE_TAG or pack["asset_name"] != pack_id + "-1.0.0.zip":
            raise ValueError(f"Unexpected source revision: {pack_id}")
        gh("release", "download", SOURCE_TAG, "--repo", REPO, "--dir", str(folder),
           "--pattern", pack["asset_name"])
        raw = (folder / pack["asset_name"]).read_bytes()
        if len(raw) != pack["bytes"] or hashlib.sha256(raw).hexdigest() != pack["sha256"]:
            raise ValueError(f"Archive checksum mismatch: {pack_id}")
        with zipfile.ZipFile(io.BytesIO(raw)) as archive:
            if {x for x in archive.namelist() if not x.endswith("/")} != {e["path"] for e in pack["entries"]}:
                raise ValueError(f"Archive content mismatch: {pack_id}")
            assets = {}
            for entry in pack["entries"]:
                data = archive.read(entry["path"])
                if len(data) != entry["bytes"] or hashlib.sha256(data).hexdigest() != entry["sha256"]:
                    raise ValueError(f"Asset checksum mismatch: {entry['path']}")
                assets[entry["path"]] = (copy.deepcopy(entry), data)
        selected.append((pack, assets))
    return selected


def bundle(originals, output):
    paths = {}
    targets = {}
    for pack, assets in originals:
        for name, (entry, data) in assets.items():
            target = entry["target"].lower()
            if name in paths and paths[name][1] != data:
                raise ValueError(f"Conflicting archive filename: {name}")
            if target in targets and targets[target][1] != data:
                raise ValueError(f"Conflicting target path: {target}")
            paths[name] = (entry, data)
            targets[target] = (entry, data)
    if sum(e["target"].lower().endswith(".glb") for e, _ in targets.values()) != 3:
        raise ValueError("Expected exactly three GLB models, A/B/C")
    with zipfile.ZipFile(output, "w") as archive:
        for name in sorted(paths):
            entry, binary = paths[name]
            item = zipfile.ZipInfo(name, date_time=(2020, 1, 1, 0, 0, 0))
            item.compress_type = zipfile.ZIP_STORED  # safe expansion ratio
            item.external_attr = 0o100644 << 16
            archive.writestr(item, binary)
    if any(pack["license"] != originals[0][0]["license"] for pack, _ in originals):
        raise ValueError("Source licenses disagree")
    merged = copy.deepcopy(originals[0][0])
    merged.update(id=NEW_ID, name="Kenney Characters Trio (A, B, C)",
                  description="Three lightweight Kenney Blocky Characters: A, B, and C.",
                  category="Characters", version="1.0.0", tag=NEW_TAG,
                  asset_id=1, asset_name=NEW_ZIP, bytes=output.stat().st_size,
                  sha256=hashlib.sha256(output.read_bytes()).hexdigest(),
                  entries=[paths[n][0] for n in sorted(paths)], dependencies=[], materials=[])
    return merged


def retired(pack):
    return pack["id"] in RETIRED or re.fullmatch(r"character-[a-r]", pack["id"]) is not None


def replace(catalog, new_pack):
    if not isinstance(catalog, dict) or not isinstance(catalog.get("packs"), list):
        raise ValueError("Unknown manifest layout: abort without publishing")
    entries = catalog["packs"]
    if any(not isinstance(p, dict) or not isinstance(p.get("id"), str) for p in entries):
        raise ValueError("Unknown pack entries: abort without publishing")
    revised = copy.deepcopy(catalog)
    revised["packs"] = [p for p in entries if not retired(p) and p["id"] != NEW_ID] + [copy.deepcopy(new_pack)]
    ids = [p["id"] for p in revised["packs"]]
    if len(ids) != len(set(ids)) or any(retired(p) for p in revised["packs"]):
        raise ValueError("Duplicate or retired asset survived catalogue filtering")
    return revised


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--publish", action="store_true")
    args = ap.parse_args()
    actor = json.loads(gh("api", "user"))["login"]
    if args.publish and actor.lower() != "aeowun":
        raise ValueError(f"Expected Aeowun GitHub account, got {actor}")
    if release(NEW_TAG) is not None:
        raise ValueError(f"{NEW_TAG} already exists; inspect the published revision")
    with tempfile.TemporaryDirectory(prefix="worldkiln-trio-") as root:
        workspace = Path(root)
        old_sources, _ = manifests(SOURCE_TAG, workspace)
        current, v2 = manifests(BASE_TAG, workspace)
        originals = sources(old_sources, workspace)
        zip_path = workspace / NEW_ZIP
        new_pack = bundle(originals, zip_path)
        primary = replace(current, new_pack)
        second = replace(v2, new_pack) if v2 is not None else None
        print(f"Validated {NEW_ZIP}: {new_pack['bytes']} bytes, exactly 3 character GLBs")
        print(f"Catalogue packs: {len(current['packs'])} before; {len(primary['packs'])} after")
        if not args.publish:
            print("Dry run complete; no GitHub release changed. Publish requires --publish.")
            return
        gh("release", "create", NEW_TAG, "--repo", REPO,
           "--title", "Worldkiln Optional Assets v1.6.0 — Kenney Characters Trio",
           "--notes", "Retires Little Elf Animated and the large Kenney character selection in the current catalogue. Adds one lightweight Kenney three-character pack (A, B, C). Previous release archives and user projects remain unchanged.")
        gh("release", "upload", NEW_TAG, str(zip_path), "--repo", REPO)
        info = release(NEW_TAG)
        asset = next((a for a in info["assets"] if a["name"] == NEW_ZIP), None)
        if asset is None or asset["size"] != new_pack["bytes"] or asset.get("digest") != "sha256:" + new_pack["sha256"]:
            raise ValueError("Published archive checksum/identity failed: DO NOT publish manifest")
        for catalogue in (primary, second):
            if catalogue is not None:
                next(p for p in catalogue["packs"] if p["id"] == NEW_ID)["asset_id"] = asset["id"]
        main_manifest = workspace / "assets-manifest.json"
        main_manifest.write_text(json.dumps(primary, indent=2) + "\n", encoding="utf-8")
        gh("release", "upload", NEW_TAG, str(main_manifest), "--repo", REPO)
        if second is not None:
            v2_file = workspace / "assets-manifest-v2.json"
            v2_file.write_text(json.dumps(second, indent=2) + "\n", encoding="utf-8")
            gh("release", "upload", NEW_TAG, str(v2_file), "--repo", REPO)
        print(f"Published https://github.com/{REPO}/releases/tag/{NEW_TAG}")


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(f"NOT PUBLISHED: {exc}", file=sys.stderr)
        sys.exit(1)
