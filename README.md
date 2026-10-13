# Worldkiln — Optional Asset Packs

**Independent asset downloads.** This repository hosts **optional** asset-only GitHub Releases for Worldkiln, separately from engine installers and release candidates. No pack is required to create a blank project.

## Small downloads — now available

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

**Download:** See the [current combined catalogue v1.1.0](https://github.com/Aeowun/Worldkiln-AssetPacks/releases/tag/asset-packs-v1.1.0) or the [original five complete packs v1.0.0](https://github.com/Aeowun/Worldkiln-AssetPacks/releases/tag/asset-packs-v1.0.0). Every pack can be downloaded independently. Engine downloads stay in [Worldkiln](https://github.com/Aeowun/Worldkiln/releases).

**Compatibility status:** Pack archives have been checked for source licensing, ZIP integrity, valid GLB headers and dependency files, and checksums. **Live Worldkiln editor imports, animated character behavior and project installation have not yet been visually tested.** Published Worldkiln 0.8.7 builds still require an engine update before this **separate repository** appears in the editor. The local Worldkiln development checkout contains an experimental dual-repository catalogue loader, which must pass technical/editor verification before release. No installer or existing engine release assets are changed by publishing these archives.

## Distribution rules

- Accept only freely redistributable sources with verifiable licenses; reject any asset with unclear rights.
- Record the upstream creator, original source URL, original archive checksum and included license in each ZIP.
- Never ship asset packs as mandatory engine data or silently install them.
- Keep pack versions and SHA-256 checksums immutable once published. Issue a new release for replacements.
- Preserve user-owned content. Do not overwrite existing project assets silently.

CC0 license details: https://creativecommons.org/publicdomain/zero/1.0/
