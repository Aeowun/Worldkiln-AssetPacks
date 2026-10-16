# Worldkiln — Optional Asset Packs

**Independent asset downloads.** This repository hosts **optional** asset-only GitHub Releases for Worldkiln, separately from engine installers and release candidates. No pack is required to create a blank project.

## Current in-editor catalogue: v1.6.0

The [v1.6.0 asset catalogue](https://github.com/Aeowun/Worldkiln-AssetPacks/releases/tag/asset-packs-v1.6.0) contains **15 optional packs** in the standard manifest and **19** in the extended versioned manifest. The Character selection now provides one **Kenney Characters Trio** pack with three GLBs (Characters A, B and C) plus their required PNG textures and Kenney CC0 license/source records.

- [Download Kenney Characters Trio (90 KB)](https://github.com/Aeowun/Worldkiln-AssetPacks/releases/download/asset-packs-v1.6.0/kenney-characters-trio-1.0.0.zip).
- [Standard v1.6.0 manifest](https://github.com/Aeowun/Worldkiln-AssetPacks/releases/download/asset-packs-v1.6.0/assets-manifest.json) and [extended v2 manifest](https://github.com/Aeowun/Worldkiln-AssetPacks/releases/download/asset-packs-v1.6.0/assets-manifest-v2.json).

**Little Elf Animated** and the full **Kenney Blocky Characters** selection are no longer offered by the latest catalogue. Historic published archives remain available for existing installations, and existing creator-owned project assets are not deleted. Click **Refresh** in the editor's Asset Catalogue to retrieve the latest manifest.

## Archived curated catalogue: v1.3.0

The [v1.3.0 game-building catalogue](https://github.com/Aeowun/Worldkiln-AssetPacks/releases/tag/asset-packs-v1.3.0) offers **13 optional asset-only packs** from this repository, plus the two existing Starter Material packs from the Worldkiln engine release: **15 selectable choices total**. Blank/offline projects do not require any asset pack.

**Native-install verified replacements:**
- [Kenney Pirate Kit v2.2.0](https://github.com/Aeowun/Worldkiln-AssetPacks/releases/download/asset-packs-v1.3.0/kenney-pirate-kit-2.2.0.zip) — 130 native Actors in the isolated project test.
- [Kenney Survival Kit v2.1.0](https://github.com/Aeowun/Worldkiln-AssetPacks/releases/download/asset-packs-v1.3.0/kenney-survival-kit-2.1.0.zip) — 91 native Actors.
- [Pirate Props v1.1.0](https://github.com/Aeowun/Worldkiln-AssetPacks/releases/download/asset-packs-v1.3.0/pirate-props-1.1.0.zip) — 16 native Actors.

Worldkiln does not yet support node-animated chests as static Actors. These compatible variants **retain chest meshes and material references but make the chests static**, omitting their original `open`, `close` and `open-close` glTF animation clips. **The original animated archives remain unchanged in the earlier v1.0.0 and v1.1.0 releases**. No other packaged model or texture contents were changed for the three replacements. Every pack keeps original Kenney CC0-1.0 licensing and origin records.

**Asset Catalogue PNG artwork:** All **15 catalogue choices** now have public preview PNGs: six original themed Pirate/Survival images and twelve additional `catalogue_*.png` attachments. The catalogue selects one relevant image per pack. Model-pack artwork illustrates the actual ZIP-contained GLB geometry with simplified shading; the two starter Material collages show real pack BaseColor textures. These files are not Worldkiln Editor/Play screenshots. The Asset Manager and Content Browser use a separate live GLB geometry renderer rather than these PNGs.

[Download the archived v1.3.0 manifest](https://github.com/Aeowun/Worldkiln-AssetPacks/releases/download/asset-packs-v1.3.0/assets-manifest.json). Original releases remain accessible for existing pack dependencies.

## Archived curated catalogue: v1.2.0

The [v1.2.0 catalogue](https://github.com/Aeowun/Worldkiln-AssetPacks/releases/tag/asset-packs-v1.2.0) first reduced the list to 15 selectable game-building choices but included three packs blocked by animated chests. It remains available for historical reference, not recommended for new installation.

## Archived extended selection: v1.1.0

The [v1.1.0 release](https://github.com/Aeowun/Worldkiln-AssetPacks/releases/tag/asset-packs-v1.1.0) publishes **49 new micro-pack ZIPs** independently from the complete v1.0.0 packs, plus the complete Kenney Furniture Kit. The combined catalogue holds **54 selectable packs**, including 18 individual character packs, 15 single-prop packs and themed subsets of trees, plants, rocks, nature props, pirate ships, pirate props, survival camping, survival tools, chairs, tables, beds, storage and prototype texture colors. The original five complete packs remain available at v1.0.0.

- You can install **one tree, barrel, rowboat, chair, bed or individual character** without downloading the complete parent pack.
- Each download remains optional. The entire ZIP includes the original Kenney CC0 license, full source provenance, individual file digests, and any external textures actually referenced by included GLBs.
- The latest [combined assets-manifest.json](https://github.com/Aeowun/Worldkiln-AssetPacks/releases/download/asset-packs-v1.1.0/assets-manifest.json) has stable pack IDs and GitHub asset identity, size and SHA-256 for every archive, including those from v1.0.0.
- These are small curated packs, **not** a promise that every individual prop from all sets has its own pack yet. Additional single-item packs may be added without changing the engine UI.

## Initial CC0 catalogue (2026-10-13)

| Pack | Category | Supplied files | Original creator | License |
|---|---|---|---|---|
| Kenney Blocky Characters | Characters | 18 GLB models, referenced textures | [Kenney](https://kenney.nl/assets/blocky-characters) | CC0 1.0 |
| Kenney Pirate Kit | Actors/Props | 72 GLB models, referenced textures | [Kenney](https://kenney.nl/assets/pirate-kit) | CC0 1.0 |
| Kenney Nature Kit | Actors/Environment | 329 GLB models, referenced textures | [Kenney](https://kenney.nl/assets/nature-kit) | CC0 1.0 |
| Kenney Survival Kit | Actors/Props | 80 GLB models, referenced textures | [Kenney](https://kenney.nl/assets/survival-kit) | CC0 1.0 |
| Kenney Prototype Textures | Textures | 78 PNG files | [Kenney](https://kenney.nl/assets/prototype-textures) | CC0 1.0 |

**Licensing and redistribution:** Every ZIP was prepared directly from a free download on Kenney's official website. Each original source archive contains a **License.txt** explicitly identifying **Creative Commons Zero (CC0) 1.0** and linking to https://creativecommons.org/publicdomain/zero/1.0/. Redistribution, including commercial use, is permitted. The **original License.txt** and a **Source.json** document recording source URL, original archive SHA-256, and conversion notes are included under `.assets/licenses/<pack-id>/` in every downloadable pack. Attribution is not legally required, but **all content is by Kenney**; Worldkiln does not claim authorship. Source artwork is not part of Worldkiln's own code license.

**Packaging:** GLB files are retained from the original archives, together with all model-relative image dependencies. Other 3D formats are omitted to avoid duplicate assets and unsupported imports. The texture pack retains PNG files. Files are organized into Worldkiln's `.assets/characters/`, `.assets/entities/` or `.assets/textures/` categories. ZIP archives have deterministic content, archive-level SHA-256 hashes, and per-file sizes/hashes in the versioned `assets-manifest.json` release attachment.

**Download:** See the [current combined catalogue v1.6.0](https://github.com/Aeowun/Worldkiln-AssetPacks/releases/tag/asset-packs-v1.6.0) or the [original five complete packs v1.0.0](https://github.com/Aeowun/Worldkiln-AssetPacks/releases/tag/asset-packs-v1.0.0). Every pack can be downloaded independently. Engine downloads stay in [Worldkiln](https://github.com/Aeowun/Worldkiln/releases).

**Compatibility status:** All v1.3.0 optional asset-only packs have passed Worldkiln native archive-install / clone-to-project tests on the local development checkout. The earlier 13-pack audit found the three chest-animation failures; the v1.3.0 replacements resolved them without changing old source archives. This does not certify live Editor/Play visuals or standalone-game packaging. Published editor versions may not yet include the source changes used in these tests. No installer or existing engine release assets were changed by publishing the asset-only release.

## Distribution rules

- Accept only freely redistributable sources with verifiable licenses; reject any asset with unclear rights.
- Record the upstream creator, original source URL, original archive checksum and included license in each ZIP.
- Never ship asset packs as mandatory engine data or silently install them.
- Keep pack versions and SHA-256 checksums immutable once published. Issue a new release for replacements.
- Preserve user-owned content. Do not overwrite existing project assets silently.

CC0 license details: https://creativecommons.org/publicdomain/zero/1.0/
