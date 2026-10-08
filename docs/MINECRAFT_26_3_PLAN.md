# Minecraft Java Edition 26.3 — independent browser port

**Status: planning and input validation. NOT PLAYABLE.**

This branch targets Java Edition 26.3 without Gaius. The inherited repository
is an experimental **26.2 TeaVM runtime/demo**; it does not contain a complete
Minecraft client. Do not label its canvas demo as gameplay.

## Build boundary

- Use a **legitimately obtained local** Minecraft Java Edition 26.3 client and
  corresponding mappings and resources.
- Never commit game source, client JARs, or copyrighted assets to this public
  repository. Apache-2.0 on the workspace does **not** license Minecraft.
- Run `python3 tools/check_263_input.py /path/to/your/private/26.3/source`
  to inventory local Java sources before attempting compatibility work.
- Stage private code under `port-src/minecraft-26.3/` locally (gitignored).
  This validator does not decompile or copy the game.
- Add proper 26.3 client entry integration, adapt LWJGL/GLFW/Vulkan/OpenGL,
  native libraries, asset indexing, storage, audio and networking to browser
  equivalents. TeaVM alone cannot make desktop APIs work.
- Compare against the actual Java client, with browser gameplay tests for
  world creation, rendering, input, audio, saving and multiplayer.
- Only publish a playable Web URL after a real browser smoke test **and**
  after validating the rights to host the resulting artifacts.

## Current status
| Component | Status |
| --- | --- |
| Upstream runtime / TeaVM demo | Present, for **26.2** |
| Private 26.3 source inventory validator | Added on this branch |
| 26.3 game source integrated | Not done |
| 26.3 rendering / audio / filesystem patches | Not done |
| Actual 26.3 main menu and gameplay tested | Not done |
| Hosted playable 26.3 URL | Not available |

This project is separate from the previous local Gradle project and Gaius.

## Build verification (2026-10-08)

The GitHub Actions source inventory unit tests completed successfully:
https://github.com/manuellynogueira10-tech/eaglercraft-262-workspace/actions/runs/37776770841

This verifies the **input validator only**, not the game, TeaVM client build,
Minecraft assets, WebGL rendering, or a deployed game. The public repository
contains none of the proprietary client source required for Java Edition 26.3.

### Honest release gate

A browser link may be called "Minecraft Java 26.3 playable" only after:
1. Genuine licensed 26.3 inputs are integrated in a private build;
2. The native graphics/audio/storage/networking APIs have functioning Web substitutes;
3. The actual Java 26.3 menu creates a world and renders its blocks and entities;
4. Saves survive browser restart and controls work in the target browsers;
5. A verified legal distribution route exists for the build and its game assets.

A hosted TeaVM canvas demo is **not** sufficient for any of these tests.
