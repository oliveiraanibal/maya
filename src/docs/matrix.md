# Multimodal Matrix

Every task can be done by voice alone or touch alone; Maya's speech always has captions, and every chime has a visual twin.

## Principles

1. **Parity:** every task can be completed by voice alone or by touch alone. A single-mode step is a bug.
2. **Mirroring:** everything Maya says appears as a caption, and every chime has a visual twin.
3. **Panoramic Vision carries nothing unique.** Anything shown there is also on the Central Display, and it cannot be touched.
4. **Voice is for intent, touch is for precision** (drag, pick, correct), but each can do the other's job.
5. **No time pressure on undo or correction,** so people who are slower to speak or tap are not penalised.
6. **Only the signed-in user commands Maya.** Other occupants' speech is context only, and edits on the Central Display are tied to the signed-in user.
7. **Without you, the phone is the window.** When the car runs an errand alone, nobody is in the cabin to see the Central Display or hear Maya, so the run is followed and reported on Michael's phone: view only, through notifications, never by voice.

## Channels

| | Input | Output |
|---|---|---|
| Voice | Natural language, always listening in the cabin (ambient intent) | Maya's spoken lines (rare) |
| Touch | Central Display: tap, drag, type, pick | Central Display: all detail and interaction |
| Cabin camera | Face at sign-in (S01); in courier mode, the empty-cabin and item checks | none (results appear on the Central Display or the phone) |
| Panoramic Vision | none (not touchable) | Glance: presence, next stop, spare time, events; off when the cabin is empty |
| Chime | none | Ambient changes only, always with a visual twin |
| Captions | none | Text of anything Maya says, on the Central Display |
| Phone (courier mode only) | Tap a notification to open the run or the report; view only | Live run (C2), errand report (C3), notifications; never voice |
| Car exterior (courier mode only) | The shop staff type the one-time code at the door | The door to use flashes; only that door opens, then it locks |

## Task matrix

**Boarding and briefing**

| Task | Voice | Touch | Central Display shows | Panoramic Vision shows |
|---|---|---|---|---|
| Sign in | Face recognition, no words needed | PIN or password, or Switch profile (S01) | Sign in (S01), then Welcome and "Going home" (S02) | Home and arrival time, once signed in |
| Adjust Maya's access | "Change what you can access" | Tap Adjust on the welcome screen (S02) | Maya's access (S03) | none |
| Start Maya | Speak at any time | Tap Maya's bar at the bottom to type (S05) | Briefing (S04) | ◉ listening |
| State needs and goals | Speak freely | Type on the keyboard (S05) | The "New plan" card fills in (S04) | ◉ listening |
| Answer Maya's question | Say it | Type in the search field (S06) | The card updates (S06) | ◉ listening |
| Accept or decline a suggestion | "Yes, white roses" / "No thanks" | Tap Yes, order or No thanks (S10) | Florist card (S10), then the order steps (S11) | ◉ speaking, then ◉ on call |

**Planning and editing**

| Task | Voice | Touch | Central Display shows | Panoramic Vision shows |
|---|---|---|---|---|
| Review the plan | "What's next?" | Tap a stop on the timeline | Timeline, map, stop detail (S12) | Next stop and spare time |
| Move a stop | "Pick up my wife before the pharmacy" | Drag the stop in Edit plan (S15) | Ripple preview, then Apply (S15) | Event "Plan updated" |
| Remove or add a stop | "Skip the pharmacy" / "Add a stop at..." | Remove, or Add stop, in Edit plan (S15) | Updated plan | Event "Plan updated" |
| Undo a change | "Undo that" | Tap Undo (S14, S17) | Plan reverts | Event "Plan updated" |

**In transit**

| Task | Voice | Touch | Central Display shows | Panoramic Vision shows |
|---|---|---|---|---|
| Check status | "Are we on time?" | Look at spare time, always on screen | Spare time and stop times (S14) | Spare time |
| Know what the car will do at a stop | "What happens at school?" | Read the intent card (S13) | Where it stops, which doors unlock, how long it waits (S13) | Next stop |
| Follow retailer calls | Not needed (silent) | Open the live transcript | Transcript with hold timer (S08) | ◉ on call |
| Answer a phone call | "Answer" | Tap Answer | Call overlay (S16) | none |
| Dismiss an alert | "Dismiss" | Tap Dismiss | Clears | Clears |

**Courier errands**

| Task | Voice | Touch | Central Display or phone shows | Panoramic Vision shows |
|---|---|---|---|---|
| Accept or decline a suggested errand | "Yes, please" / "No thanks" | Tap Yes or No thanks (S18) | Errand suggestion (S18), then the call, payment and agreed handover (S19) | ◉ speaking, ◉ on call, then "Errand booked: dry cleaner" |
| Schedule an errand by hand | "Drop my jacket at the dry cleaner tomorrow at 10" | Box icon, then New errand (C4, C5) | Errands list and form (C4, C5) | Event "Errand booked" |
| Choose the handover | "Put it in the boot" | Pick a door or the boot on the top view of the car (C5) | Top view with the chosen compartment | none |
| Follow the run | Not needed (notifications) | Open the notification | Phone: live map and steps (C2) | Off (cabin empty) |
| Read the report | Not needed (notification) | Open the notification | Phone: photo, receipt, times, what the camera saw (C3) | Off (cabin empty) |

## Output matrix: what each event produces

| Event | Central Display | Panoramic Vision | Voice | Chime | Caption |
|---|---|---|---|---|---|
| Maya asks a question | Question card | ◉ speaking | Yes | No | Yes |
| Automatic plan update (pharmacy) | Banner and ledger (S09) | Event, 4 s | No | No | n/a |
| **Ambient change (pickup)** | Heard phrase, crossed and new stops, Undo (S17) | Event, 4 s | **No** | **Yes** | n/a |
| Retailer call | Live transcript (S08) | ◉ on call | No | No | Transcript |
| Errand booked | Call, payment and handover steps (S19) | ◉ on call, then event, 4 s | No | No | Transcript |
| Vehicle intent before a stop | Intent card (S13) | Next stop | No | No | n/a |
| Spare time shrinking | Green above 4 min, amber 0 to 4, red below 0 | Same colours, "+2 min" | No | No | n/a |
| Running late | Fixes, cheapest first (V2) | Red, with a minus sign | Yes (short) | No | Yes |
| Pickup states | State chip | Next stop | No | No | n/a |
| Arrival | Arrival report (S20) | Arrived and spare time | Yes (short) | No | Yes |
| Courier hand-off | "Leaving in courier mode. Please take your belongings." (C1) | "Courier · waits for you" | Yes, in the arrival line | No | Yes |
| Error or offline | Error card with action | "Offline · plan kept" | No | No | n/a |

Only ambient changes use the chime. Every other alert, including low spare time and offline, is visual; Maya speaks only when she needs an answer or has a result.

**Courier mode outputs**

Nobody is in the cabin, so during the run there is no voice and no chime, and the Central Display and Panoramic Vision are off. Everything goes to Michael's phone, and the car speaks to the shop staff only through one flashing door.

| Event | Phone | Car exterior | Cabin |
|---|---|---|---|
| Something left in the cabin (before leaving) | Notification: courier on hold until it is removed | none | Central Display shows what and where; Maya says it once, with a caption |
| Car leaves (18:58) | Live run starts (C2) | none | Central Display and Panoramic Vision off |
| At the shop (19:20) | Step: at the dry cleaner | Rear right door flashes; the code opens only that door | Camera checks the item: "1 garment bag, rear right" |
| Report (19:24) | Notification and report (C3) | Door locked | none |
| The errand runs late | Notification with the new time | none | none |

## Stress tests

| Situation | What it exposes | Fix |
|---|---|---|
| **Touch-only user** (speech-impaired) | Ambient intent only hears others, never them | They instruct by touch; ambient intent still works on calls and messages |
| **Voice-only user** (motion-impaired) | Undo and edits need a tap | Every action has a spoken command, and undo has no short timeout |
| **Noisy cabin** | Voice misses or errors | After one failed attempt, Maya shows the touch path on the Central Display instead of asking again |
| **Hard of hearing** | The chime is missed | Visual twin on both the Central Display and Panoramic Vision, and optional haptics |
| **Children tapping the Central Display** | Accidental edits | Edit actions tied to the signed-in user's profile |
| **Privacy** (silent mode) | The user does not want to speak aloud | Full touch path, and Maya's speech becomes captions only |
| **Nobody in the car** (courier mode) | No one sees the Central Display or hears Maya, and the shop staff are not users | The phone is the window, view only; the staff get a code by text and one flashing door, and nothing else in the car responds to them |
