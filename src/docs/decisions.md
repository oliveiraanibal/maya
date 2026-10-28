# Decision Log and Trade-offs

This log records what we decided for Maya, what each choice costs us, and which costs we expect but have not yet decided.

## Decisions of 28 October 2026

Phase 0 is closed. These choices now apply to every artifact.

| Topic | Decision |
|---|---|
| Final deliverable | One self-sufficient PDF, Anibal-Oliveira_CTW-UX-Challenge_Maya.pdf: everything needed to judge the work is inside it |
| Links from the PDF | Extras, not needed to judge the work. At most three, hosted as plain web pages on GitHub Pages so nobody has to sign in: clickable prototype, hi-fi screens, process index. Each one tested in a private window |
| Screen IDs | Renumbered once, in story order: S01 to S20 in the car, C1 to C5 for courier mode, V1 and V2 for variants (map below). Strip states take the ID of the screen they go with |
| The user | Called Michael in every screen and doc. Aníbal Oliveira stays as the author |
| UI font | Inter, replacing Manrope |
| Language | UK English everywhere |
| Sign-in | New first screen (S01). The car expects Michael but signs him in only after face recognition; PIN or password as fallback; "Not Michael? Switch profile" |
| Errands entry | A box icon left of the settings cog on every tablet screen opens Errands (C4). The bento icon stays top left, with "Maya" to its right and more space between them; the bento menu itself (other apps) is not designed |
| Courier mode | In scope. The story's errand is the dry cleaner, offered after the hair salon pickup (scene 8) |
| Charging | Not an errand, so it never appears in the plan list |
| Story end | The story ends with the car charging near the restaurant after the courier errand. The return at 21:30 is promised, not shown: the same car, with the suit, charges near the restaurant until Michael calls it, as he did at 17:15 |
| Phone | Courier mode only and view only, kept to two screens: the live run (C2) and the report (C3). No Come back now, no voice |
| Strip in an empty car | Off once the cabin is empty. During the hand-off it shows "Courier · back 21:30" |
| Maya and the car | Maya belongs to Michael, not to a car: she is in any car he signs in to, his own or a robotaxi. In the story it is the same car all evening, because his suit is inside |
| Starting Maya by touch | No mic button: tapping Maya's bar at the bottom opens the keyboard (S05) |
| The word "errand" | An errand is something the car does alone, in courier mode. With Michael on board, the plan has stops, and the briefing card lists to-dos (the prescription is a to-do) |
| Visual direction | Deep ocean: dark first, a deep blue-green ground with cobalt and lumen glows, inspired by The Abyss. The light versions are parked; the strip is always dark |
| Shapes and surfaces | Sharp corners and no borders; translucent glass panels over a full-bleed map; spacing, not lines, groups things |
| Tablet canvas | 1920 × 1200 (16:10) |
| Map | A real-looking map of Porto that shows the whole journey; square pins, sonar rings on the next stop |
| Maya's presence | No orb: presence is a status line in Maya's bar (listening, thinking, speaking, on a call) and a pulsing dot on the strip |
| Strip | One band at the base of the windscreen, always dark: the automotive half and Maya's half, with no dividers or pill borders |
| Payments | Maya Wallet: automatic up to the limit set in Maya's access (S03); above it, Maya asks first |
| Design system | Our own Deep ocean tokens; Material 3 and Android Automotive guidance only as a reference for sizes and behaviour |
| Maya's first greeting | Spoken and short, with a caption (S02) |
| Ledger depth | "Done for you" shows the last two actions; the rest on tap (S14) |
| Arrival report | The full list of what was done, readable in one glance (S20) |
| Touch targets | Buttons keep their visual size, but every tap area is at least 76 × 76 px: the Android for Cars minimum of 76 dp, assuming about 1 px per dp on a 14 to 15 inch 1920 × 1200 tablet. Noted in the spec |
| Readability | No text below 16 px on the tablet, except uppercase labels (13 to 14 px) and small badges (12 px) |
| Errands badge | A small dot on the box icon while an errand is booked or running |

## Screen ID map

| New ID | Screen | Old ID | Scene |
|---|---|---|---|
| S01 | Sign in | new | 1 |
| S02 | Welcome | S1 | 1 |
| S03 | Maya's access (from Adjust) | N3 | 1 |
| S04 | Briefing: listening | S2a | 2 |
| S05 | Briefing: keyboard | S2d | 2 |
| S06 | Briefing: Maya asks | S2b | 2 |
| S07 | Briefing: building the plan | S2c | 2 |
| S08 | Retailer calls | S3 | 3 |
| S09 | Plan change: automatic | S7a | 3 |
| S10 | Gift suggestion | S4a | 4 |
| S11 | Florist order | S4b | 4 |
| S12 | Plan overview | S5 | 5 |
| S13 | Vehicle intent | N1 | 6 |
| S14 | Active trip | S6a | 6 |
| S15 | Edit plan | S8 | 6 |
| S16 | Incoming call | S6b | 7 |
| S17 | Plan change: ambient | S7b | 7 |
| S18 | Errand suggestion | new | 8 |
| S19 | Errand booked | new | 8 |
| S20 | Arrival report | S9 | 9 |
| C1 | Leaving in courier mode | new | 9 |
| C2 | Phone: courier run | new | 10 |
| C3 | Phone: errand report | new | 10 |
| C4 | Errands (box icon) | new | any time |
| C5 | New errand | new | any time |
| V1 | Takeover request (Level 3/4 variant) | N2 | variant |
| V2 | Running late | N4 | edge case 2 |

## Accepted trade-offs

| Decision | What we gain | What we give up | Where it shows | Check it by |
|---|---|---|---|---|
| Level 5 only, no manual driving | A single calm, trip-level experience | Any use before full autonomy; no driver-state design | Hypothesis | n/a |
| Full trust: Maya acts, pays and listens | The assistant feels like an executive assistant | Safety nets: no approval before calls, or before payments under the limit set in Maya's access (S03) | S02, S03, S11 | Trust calibration (month list) |
| Maya speaks rarely; the screen carries the detail | A quiet cabin; calm trip | Users who rely on voice alone get less status | Multimodal Matrix, S08 | Voice-only stress test |
| Ambient intent: Maya acts on high confidence and asks on medium | Plans change without the user managing them | Risk of false positives from overheard talk | S17 | Ambient false-positive test |
| Chime only for ambient changes, with the heard phrase and Undo, no countdown | Non-intrusive; a missed chime costs nothing | A user may not notice a change until they look | S17 | Validation plan |
| Banner stays until dismissed | Never lost | Panel clutter if changes pile up | S09 | Prototype |
| Pharmacy first, flowers after | The urgent to-do wins | Flowers are offered later, with less lead time | S08, S10 | Prototype |
| Silent retailer calls shown on screen only | Silence in the cabin | Users cannot hear what Maya promised | S08 | Wizard of Oz (month list) |
| Passive LED strip carrying nothing unique | No second interactive surface to design | Strip cannot be the only channel for anything | Screen Plan | n/a |
| One tablet layout: plan panel always left, flat 2D map | Learnable and consistent | No right-to-left variant; no 3D context | Wireframes | Responsive layouts (month list) |
| Keyboard takes about the lower half of the screen | Large, comfortable keys | Plan and map shrink while typing | S05 | Prototype |
| Undo only on the latest ledger row, then the previous | A calm ledger, one clear action | Older actions are slower to reverse | S14 | Prototype, 3 users |
| Spare time pill: green above 4 min, amber 0 to 4, red below 0 | Promise readable at a glance | Colour alone is not enough: needs text and shape too | S12 to S20 | Accessibility review |
| Edit plan with ripple preview, then Apply | Informed edits | Extra step for a quick change | S15 | Prototype |
| Solo exercise with no user research | Speed | Assumptions A1 to A15 are untested | Hypothesis | Validation plan |

## Courier mode: rules and trade-offs

Courier mode lets the empty car run errands. It starts only when nobody is inside and the handover has been agreed.

| Rule | What we gain | What we give up | Where it shows | Check it by |
|---|---|---|---|---|
| Empty cabin only: before leaving, the car checks for people, pets and forgotten items | Nobody rides along by accident | A camera in the cabin | C1 | Courier trust test |
| No handoff, no commitment: an errand is booked only once the other side confirms the time, the person and the handover | Errands don't fail at the door | Fewer errands qualify | S19, C5 | Prototype |
| One door, one code: only the agreed compartment opens, with a one-time code, and the camera checks what goes in or out | The rest of the car stays closed | The item must fit that compartment | S19, C2, C5 | Prototype |
| The return time is the promise | Michael knows when the car will be back | Errands that can't make it are declined or moved | S18, C2 | Prototype |
| Every run is reported: live on the phone, then a photo, receipt and times | Trust without watching | A third surface, the phone | C2, C3 | Courier trust test |
| Charging is not an errand | A short, clear plan | Charging happens out of sight | S19, S20 | n/a |
| Errands open from a box icon beside Settings | Errands are one tap away on any screen | One more icon in the corner | All tablet screens | Prototype |
| Pick-ups and drop-offs only, for now | A simple form | Other errand types come later | C5 | n/a |

## Expected trade-offs, not yet decided

| Open question | Option A | Option B | Lean | Decide at |
|---|---|---|---|---|
| What happens when Maya is unsure on a payment | Ask first | Act and show Undo | Act and show Undo, below a limit | Month list |
| Responsive layouts (other screen sizes and orientations) | Scale the tablet layout | Design each size | Design each size | Month list |

## Screens for later

These are not delivered now. Each one is a gap in the current story, not a decision.

- Bento menu contents (other apps); the icon stays top left
- Create new profile
- Idle or standby, when nobody is signed in
- Guest mode
