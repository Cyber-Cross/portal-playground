# Portal Playground

A Portal-inspired 3D physics sandbox that runs in the browser. No levels, no rules: shoot portals, spawn props, and fling things (and yourself) around a test chamber.

Built with [Three.js](https://threejs.org/) for rendering and [cannon-es](https://github.com/pmndrs/cannon-es) for physics. No install and no build step required to play.

## Play

Option 1: GitHub Pages — visit https://cyber-cross.github.io/portal-playground/

**Option 2: offline file .** Download [`Portal-Playground-offline.html`](Portal-Playground-offline.html) and open it in Chrome, Edge, Firefox, or Safari. Everything is bundled into that one file, so it works without an internet connection.

**Option 3: from source.** Open `index.html` through a web server. It loads Three.js and cannon-es from the unpkg CDN, so it needs an internet connection. For example:

```sh
python3 -m http.server 8000
# then visit http://localhost:8000
```

`index.html` also works as-is on GitHub Pages.

## What's in the playground

- **Portals:** shoot a blue and an orange portal onto white surfaces. Anything entering one exits the other with its momentum intact.
- **Props:** Companion Cube, Crate, Basketball, Bouncy Ball, Beach Ball, Bowling Ball, Boom Barrel, Mega Cube, plus a Domino Row and Prop Rain.
- **Gels and launchers:** blue gel bounces you, orange gel speeds you up, Faith Plates launch you, red barrels explode.
- **Flings:** jump off the central tower into a floor portal and come out of an angled panel.
- **Basketball court:** a shot that passes through a portal first is worth 3 points.
- **Rings:** fly through the floating orange rings to collect them all. Stay out of the green goo.

## Controls

| Input | Action |
|---|---|
| WASD / Space / Shift | Move / Jump / Sprint |
| Left click | Blue portal (throws a held object) |
| Right click | Orange portal (drops a held object) |
| E | Pick up / drop |
| 1-0 or scroll wheel | Select prop |
| F or middle click | Spawn selected prop |
| R / C | Clear portals / Clear spawned props |
| G / T | Low gravity / Slow motion |
| Esc | Pause |

The Options menu also toggles shadows, high-quality portal rendering, and an FPS counter.

## Project layout

| File | Purpose |
|---|---|
| `index.html` | The game source (HTML, CSS, and an ES module). Pulls Three.js and cannon-es from unpkg via an import map. |
| `build-offline.py` | Builds `Portal-Playground-offline.html` by inlining Three.js and cannon-es as classic scripts, so the game runs straight from disk with no network or ES module support. |
| `Portal-Playground-offline.html` | Prebuilt single-file version of the game. |

## Rebuilding the offline file

After editing `index.html`, regenerate the offline build:

```sh
python3 build-offline.py
```

The first run downloads Three.js 0.160.0 and cannon-es 0.20.0 into `vendor/` (ignored by git). Later runs reuse the cached copies.

## License

[MIT](LICENSE). Three.js and cannon-es are also MIT licensed and are bundled into the offline build.

Portal is a trademark of Valve Corporation. This is an unofficial fan project and is not affiliated with or endorsed by Valve.
