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
