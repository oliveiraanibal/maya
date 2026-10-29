# Concept Foundations

## Context

Maya is an AI concierge inside a fully autonomous (Level 5) car. She plans and runs the logistics of a single trip: routing, stops and calls to retailers. Michael, the user in our story, is in the car and either talks to her or uses the Central Display; Panoramic Vision, a passive band at the base of the windscreen, shows glanceable status. Maya acts with full delegated trust, like an executive assistant, within the limits Michael sets, and he can see and undo everything. Maya belongs to Michael, not to the car: she is in any car he signs in to, his own or a robotaxi. When nobody is in the car, Maya can also send it to run errands on its own (courier mode); a car in courier mode is always reserved to Michael.

## Problem

Navigation handles routes, not commitments. Even in a driverless car the passenger still has to work out the sequence of stops, phone businesses, and re-plan by hand whenever something changes, so the freed-up time is not really free.

## Vision

*I share my needs and goals; everything else just happens, and I can see it happening.*

*With me in the car, Maya runs my trip. Without me, my car runs my errands.*

## Hypothesis

We believe that time-poor people will hand over trip logistics entirely to an AI that asks only what it cannot know (as many questions as needed, no more), acts on its own, follows the conversation (ambient intent), and makes every action visible and reversible. We will know we are right when users arrive on time, rarely undo what Maya did, and trust her with more over time.

Courier mode extends the bet: people will also let an empty car run errands on its own, as long as every handover is agreed before it leaves and reported when it's done.

## Hero scenario: the family dinner run

One evening: Michael is collected at work at 17:15 and needs his kids, his wife and a new prescription before a 19:00 family birthday dinner; Maya plans, phones and replans so the family arrives at 18:55, then the empty car collects his suit from the dry cleaner. The full script and timings are in [The Scenario](../hero/).

## Scope

- **In:** sign-in by face (PIN or password as fallback) with a default route; Maya's access settings; briefing in needs and goals; a proactive suggestion tied to a known occasion; plan overview with spare time (5 min); live calls to retailers with payment from Maya Wallet; automatic reroutes; ambient intent; plan editing; two-screen UI (Central Display plus a passive Panoramic Vision band); voice and touch parity; courier mode: errands that Maya suggests or that are scheduled from the Errands button, run by the empty car with an agreed handover, followed live on the phone in the My BMW app (view only) and reported at the end.
- **Assumed, not designed:** payments happen automatically from Maya Wallet, up to the limit set in Maya's access (top-ups and statements are not designed); schools release the children to the car; Maya uses a shop's own ordering system when it has one, and phones it when it doesn't, as most local shops have none; Maya checks the car's range when she builds the plan; the same car, with the suit, charges near the restaurant until Michael calls it.
- **If I had a month:**
  - Other errand types beyond pick-ups and drop-offs
  - The app launcher's contents, creating a new profile, idle or standby when nobody is signed in, guest mode
  - When Maya is unsure about a payment: ask first, or act and show Undo (leaning towards Undo, below a limit)
  - Responsive layouts for other screen sizes and orientations (leaning towards designing each size)
  - A shared digital key for courier handovers, instead of a typed code
  - The 3D head-up display
  - Driving preferences, such as "prioritise speed over cost"
  - A full activity log, wallet top-ups and statements, and trust that grows over time
  - Multi-passenger conflicts, merchant onboarding and support escalation to a human
  - A competitive and analogous review, a proto-persona, a Wizard of Oz session, accessibility research and a study of real family trips
  - A regulation review for empty cars (A15)

## Success metrics (illustrative targets)

| Metric | Target |
|---|---|
| On-time arrival (within the 5-minute spare time) | 95% or more |
| Replans that keep spare time at or above zero | 90% or more |
| Questions Maya could have answered herself | Under 10% |
| Undo rate on automatic and ambient changes | Under 10% |
| Time from a change to a visible adapted plan | 3 seconds or less |
| Proactive suggestion acceptance | 50% or more |
| "Feels like a great assistant" rating | 4 / 5 or more |
| Courier errands completed without the user stepping in | 90% or more |
| After a courier run, the car arrives within the time shown when called | 95% or more |
| Actions moved from Ask first to Act within a month | Rising |

## Assumptions, ranked by risk

| # | Assumption | Risk | Confidence | How we would test it |
|---|---|---|---|---|
| A1 | Pre-trusted users accept "do first, show clearly, undo easily" | High | Medium | Wizard of Oz session (if I had a month) |
| A2 | Maya can predict the likely destination and learn the user's day and recurring places from habit and data (calendar, messages) | High | Medium | Prototype with a scripted calendar |
| A3 | **Ambient intent:** listening to cabin talk and calls is welcome, and false positives are cheap to undo | High | Low | Ambient-intent test |
| A4 | Retailers cooperate with a self-identified AI caller (hold, stock, payment, timing) | High | Low | Scripted calls to local shops (if I had a month) |
| A13 | Shops will hand items to, or take them from, an empty car that opens one door with a one-time code | High | Low | Scripted calls to local shops (if I had a month) |
| A14 | People will let their empty car run an errand, and accept a cabin camera that checks the cabin and the handover | High | Medium | Courier trust test |
| A15 | An empty Level 5 car may legally drive and stop on its own to run errands | High | Medium | Assumed; regulation review (if I had a month) |
| A16 | Michael's phone data (messages, calendar) is available to the car, despite the limits phone platforms set | High | Medium | Assumed; platform review (if I had a month) |
| A5 | Automatic payments from Maya Wallet, up to a limit, are acceptable | Medium | Medium | Not tested (out of scope) |
| A6 | Users accept as many questions as needed when each is clearly necessary | Medium | Medium | Wizard of Oz session (if I had a month) |
| A7 | A proactive suggestion tied to a known occasion (a birthday) is welcome | Medium | Medium | Concept test |
| A8 | Spare time (5 min) gives at-a-glance confidence | Medium | Medium | Glance test |
| A9 | Silent changes with a chime, heard phrase and Undo are understood in a noisy cabin | Medium | Medium | Replan legibility test |
| A10 | A passive Panoramic Vision band carries enough glanceable information while the Central Display holds all interaction | Medium | Medium | Glance test |
| A11 | Voice and touch parity is achievable for every task | Medium | Medium | Touch-only run |
| A12 | On-time arrival is the dominant success criterion | Medium | Medium | Short survey |

## Design principles

1. **Ask only what she can't know,** as many times as needed.
2. **Ambient intent:** the plan follows the conversation.
3. **Speak only when needed;** the screen is the confirmation.
4. **Do first, show clearly, undo easily:** no approval gates within the limits he sets, and no countdown.
5. **The plan is alive:** the world, the conversation or the user can reshape it, and the ripple is visible.
6. **Spare time is the promise:** 5 minutes, always visible; green above 4, amber 0 to 4, red below 0.
7. **Central Display to act, Panoramic Vision to glance** (Panoramic Vision carries nothing unique).
8. **Voice and touch are equals.**
9. **With you or without you:** when the car is empty it works for you, but only with an agreed handover (no handoff, no commitment).

## Conversation design rules

1. **Ask only what she can't know, as many times as needed.** Here that is two questions and one suggestion.
2. **Speak only when she needs Michael:** a question, the result of something he asked, or when the car leaves. Everything else is on screen.
3. **The screen is the confirmation.** The "New plan" card replaces reading back.
4. **Changes caused by the world happen silently and visibly.** Changes caused by conversation get a chime, the heard phrase, and Undo.
5. **Calls to staff are screen-only and transparent:** live transcript, always opening with "Hello, I'm Maya, an AI assistant calling...".
6. **Every voice action has a touch twin** (chips, pickers, drag).
7. **Maya's voice:** calm, competent, short, female. She says "we" for the trip.
8. **Medication names stay off the shared screen:** transcripts say "your prescription" and show the reference number only.
9. **Courier errands are booked only once the handover is agreed.** Maya says once what the car will do and when it will be back; the run itself is followed on the phone.

## Trade-offs

| Decision | What we gain | What we give up | Where it shows | Check it by |
|---|---|---|---|---|
| Full trust: Maya acts, pays and listens | The assistant feels like an executive assistant | Safety nets: no approval before calls, or before payments under the limit set in Maya's access (S03) | S02, S03, S11 | Trust calibration (if I had a month) |
| Maya speaks rarely; the screen carries the detail | A quiet cabin; calm trip | Users who rely on voice alone get less status | Multimodal Matrix, S08 | Voice-only stress test |
| Ambient intent: Maya acts on high confidence and asks on medium | Plans change without the user managing them | Risk of false positives from overheard talk | S17 | Ambient false-positive test |
| Chime only for ambient changes, with the heard phrase and Undo, no countdown | Non-intrusive; a missed chime costs nothing | A user may not notice a change until they look | S17 | Validation plan |
| Banner stays until dismissed | Never lost | Panel clutter if changes pile up | S09 | Prototype |
| Pharmacy first, flowers after | The urgent to-do wins | Flowers are offered later, with less lead time | S08, S10 | Prototype |
| Silent retailer calls shown on screen only | Silence in the cabin | Users cannot hear what Maya promised | S08 | Wizard of Oz (if I had a month) |
| One layout on the Central Display: plan panel always left, flat 2D map | Learnable and consistent | No right-to-left variant; no 3D context | Central Display Wireframes | Responsive layouts (if I had a month) |
| Keyboard takes about the lower half of the screen | Large, comfortable keys | Plan and map shrink while typing | S05 | Prototype |
| Undo only on the latest ledger row, then the previous | A calm ledger, one clear action | Older actions are slower to reverse | S14 | Prototype, 3 users |
| Spare time pill: green above 4 min, amber 0 to 4, red below 0 | Promise readable at a glance | Colour alone is not enough: needs text and shape too | S12 to S20 | Accessibility review |
| Edit plan with ripple preview, then Apply | Informed edits | Extra step for a quick change | S15 | Prototype |

## Courier mode: rules and trade-offs

Courier mode lets the empty car run errands. It starts only when nobody is inside and the handover has been agreed.

| Rule | What we gain | What we give up | Where it shows | Check it by |
|---|---|---|---|---|
| Empty cabin only: before leaving, the car checks for people, pets and forgotten items | Nobody rides along by accident | A camera in the cabin | C1 | Courier trust test |
| No handoff, no commitment: an errand is booked only once the other side confirms the time, the person and the handover | Errands don't fail at the door | Fewer errands qualify | S19, C5 | Prototype |
| One door, one code: only the agreed compartment opens, with a one-time code, and the camera checks what goes in or out | The rest of the car stays closed | The item must fit that compartment | S19, C2, C5 | Prototype |
| Ready when called | After the errand the car charges nearby; when Michael calls it, the phone says how soon it will arrive | The car is tied up until the errand is done | S18, C2 | Prototype |
| Every run is reported: live on the phone, then a photo, receipt and times | Trust without watching | A third surface, the phone | C2, C3 | Courier trust test |
| Charging is not an errand | A short, clear plan | Charging happens out of sight | S19, S20 | n/a |
| Errands open from a box icon beside Settings | Errands are one tap away on any screen | One more icon in the corner | All Central Display screens | Prototype |
| Pick-ups and drop-offs only, for now | A simple form | Other errand types come later | C5 | n/a |
