# Worldkiln — Optional Asset Packs

**Independent asset downloads.** This repository hosts **optional** asset-only GitHub Releases for Worldkiln, separately from engine installers and release candidates. No pack is required to create a blank project.

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

**Download:** See [asset-packs-v1.0.0](https://github.com/Aeowun/Worldkiln-AssetPacks/releases/tag/asset-packs-v1.0.0). Every pack can be downloaded independently. Engine downloads stay in [Worldkiln](https://github.com/Aeowun/Worldkiln/releases).

**Compatibility status:** Pack archives have been checked for source licensing, ZIP integrity, valid GLB headers and dependency files, and checksums. **Live Worldkiln editor imports, animated character behavior and project installation have not yet been visually tested.** The existing Worldkiln 0.8.7 catalogue downloader currently looks at releases in `Aeowun/Worldkiln`; it must be updated to discover this **separate repository** before these packs appear in the in-editor picker. Publishing this repository does **not** change the engine code, existing asset packs, or installer.

## Distribution rules

- Accept only freely redistributable sources with verifiable licenses; reject any asset with unclear rights.
- Record the upstream creator, original source URL, original archive checksum and included license in each ZIP.
- Never ship asset packs as mandatory engine data or silently install them.
- Keep pack versions and SHA-256 checksums immutable once published. Issue a new release for replacements.
- Preserve user-owned content. Do not overwrite existing project assets silently.

CC0 license details: https://creativecommons.org/publicdomain/zero/1.0/
