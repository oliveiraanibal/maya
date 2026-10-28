# Maya prototype

A click-through of the whole story (S01 to S20, C1 to C5) plus four "what if" branches (edge cases 1 to 4).
It is a player (`index.html`, `player.js`, `player.css`) driven by data. **You almost never touch the player.**

| File | What it is | Edit by hand? |
|---|---|---|
| `flow.json` | Behaviour: which screen leads where, what each tap zone does, notes, voice lines, branches, auto-advance | **Yes** |
| `zones.json` | Tap-zone rectangles, found in the mocks | No, generated |
| `shots/*.jpg` | One image per screen, rendered from the mock HTML | No, generated |
| `mocks/*.html` | Edge-case screens, derived from a base mock plus text replacements | No, generated |

## When the mocks change

1. Put the new mock HTML in `screens/live/` (same file name, or update `mock` in `flow.json`).
2. Run `npm install` once, then `npm run proto`.
3. Done: new images, tap zones that follow the elements, and a check that every link works and every screen is reachable.

Zones follow the elements because `flow.json` finds them by what they are, not by pixel position:

```json
{ "id": "adjust", "label": "Adjust access", "find": { "text": "Adjust", "exact": true }, "go": "S03" }
```

`find` accepts `{ "text": "Yes, order" }`, `{ "sel": "[aria-label=\"Keyboard\"]" }` (CSS), `nth` to pick the second match, `pad` to enlarge,
or a fixed `rect: [x, y, w, h]` when nothing in the mock can be found (for example a mock that is only an image: set `"image": "my.jpg"` on the screen).
Every zone is enlarged to at least 76 × 76 px, the Android for Cars minimum.

If a button's text changes, the build stops and says which zone it can no longer find. Update the text in `flow.json` and run it again.

## Changing behaviour

All in `flow.json`:

- **Add a screen**: add an entry under `screens` with a `mock`, `title`, `note`, a `cta` (the big button: the voice twin) and `hotspots` (the touch twin).
- **Re-route a tap**: change its `go`. Use `"back"` to return to where you came from.
- **Toast** instead of a screen: add `"toast": "text"` to a hotspot.
- **Auto-advance** (silent moments): `"auto": { "ms": 3200, "go": "S08" }`.
- **Branch** ("what if…" buttons): `"branches": [{ "tag": "Edge case 1", "label": "…", "go": "E1" }]`.
- **Edge-case screens**: `variants` lists a base mock and `[old, new]` text replacements. If the base mock changes so that an `old` text vanishes, the build tells you.
- **Icons in the top bar** (for example Errands) are in `global.hotspots`; `global.except` lists the screens that don't have them.

## Moving a zone by hand

Open the prototype with `?edit` (or press **E**). Drag a zone to move it, drag its corner to resize, Alt-drag on empty space to draw a new one,
double-click to set where it goes, Delete to remove. **Copy JSON for this screen** gives you a `hotspots` block with fixed `rect`s to paste into `flow.json`.
Edits are kept in your browser only until you paste them in (Reset clears them).

## Checks

`npm run proto` fails when: a link points to a screen that doesn't exist, a screen can't be reached from the start, a zone can't be found, or a variant's text no longer matches.
