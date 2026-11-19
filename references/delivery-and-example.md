# Horizontal Short-Drama Design Fields and a Minimal 15-Second Case

This page contains production fields and completed design examples, not blank forms. For reusable prompt shells, platform fallbacks, and separate production notes, see the [template contract](template-contract.md). Put newly filled values in project drafts or examples, not back into blank shells.

## Delivery scale

Creative Q&A provides only the necessary proposal; a complete horizontal episode hands off the fields below. Defaults are 16:9 and 1920×1080. The original 30-second gate-defense case remains a reusable action core integrated with episode goals and consequences, not automatically declared a complete episode. The 90-second structure below is a creative suggestion adaptable to 1–3-minute tasks.

## Project and asset cards

Project: `Genre/episode form | Target duration | Episode goal/change/result | World rules | Aspect/generation/delivery resolution | Active picture/action safe area/subtitle area | Minimum viewing viewport | Platform/model and tested conditions | Current request duration/single or segmented | Actual references and first/last-frame usage | Budget/iteration ceiling | Audience suitability/asset-rights status`. Confirm through [generation handoff](generation-handoff.md) before delivering input; do not fabricate unknown values.

Character: `ID/version | Fixed identity/costume | Character-local left/right/dominant hand | Weapon/ability structure | Initial scene damage | Reference responsibilities/exclusions`. Scene: `ID/state version | Top view/main axis | Left/right/depth anchor map | Interactive objects/destruction stages | Available camera paths`. See character, scene, and consistency references for detail.

Choreography: `Weapon length/weight-feel basis/center of mass/grip | Force and support | Effective range/attack line | Combination motif/branches | Openings and costs | Dynamic items awaiting validation`.

Research: `Asset | Era/region/identity or fictional scope | Form/pattern/source locator | Evidence/inference/original change | Wearing/operation | Action implications | Damage variants`.

## Horizontal episode example: 90-second gate escape

| Narrative unit | Time | In-shot information changes and action tasks | Generation planning |
|---|---|---|---|
| E01 Goal and approaching enemy | 0–15 s | A companion approaches the door with a box; the guard notices pursuers. Show box, exit, gate lever, and who blocks whom together | May be one continuous shot; split by available duration, matching end state to next opening |
| E02 Continuous exchanges | 15–45 s | Use the 30-second action core below: defend the first thrust, send companion through, withdraw to control, shut gate on spear | Unchanged, this is a 10-shot edited version. For a long take, redesign the camera path first and split GENs in action gaps, rather than joining 10 viewpoints into one shot |
| E03 Result and cost | 45–75 s | Spear tugging continues beyond the gate; guard checks injury and gate support; companion chooses an escape direction with the box. Choices continue through action and stillness | Organize new composition/spatial tasks and compress to needed runtime; do not pad with 30 seconds of unchanged holding |
| E04 New action | 75–90 s | Both begin leaving; pressure across the gate closes this scene. The user determines the next story goal | End with a clear situation, not a new major enemy or key ability |

These four rows are narrative units, not four fixed physical shots. If choosing 3–5 long-take-style continuous exchanges for the episode, restage E02 and neighboring movement for continuous photography. Each SHOT may contain several GENs; follow [generation segments](prompts-and-segments.md). Retaining 10 obvious cuts while claiming only four long takes is contradictory.

## Shot and generation handoff fields

Storyboard: `SHOT_ID | Time/net duration | Shared-frame left/center/right/depth and opening/ending positions | Attack/defense/result | Shot size/opening/ending composition/camera path | Readable contact area | Cut or long-take seam`.

Generation: `GEN_ID/parent SHOT | Selected interval | Request duration/handles | Actual input assets | Opening/ending pose/support/grip/damage | Independent events/capacity tradeoffs | Actual input text | Sound responsibilities | Seam matching | Key pass/fail criteria | Output labels`. Separate storyboard, submission settings/text, and post tasks. These production fields need not all be pasted verbatim into prompts.

Post: `CLIP_ID/source GEN | Net duration/repeated handles removed | Contact event ID | Dialogue/breath/whoosh/contact/material/environment/music/tail | Subtitles/lip sync | Desktop/phone checks`.

## Minimal standalone 15-second case

Simplifies the original 30-second gate core without abilities or preset injuries; it does not accelerate the original 10 shots into 15 seconds. A wears a dark-gray short robe and carries a short staff in the right hand; B has dark-brown bound sleeves and a two-handed spear; C wears gray-blue and holds a wooden box with both hands. This untested draft assumes character images and acceptance of segmented editing. For no images or one 15-second request, adapt through generation handoff first instead of inheriting these asset assumptions. Designs are fictional, not historically researched forms.

Scene GATE_v01: door west/screen left, corridor east/screen right, camera south; gate lever at the south end of the frame. Proposed timing: lever operated near 7.5 seconds, gate reaches spear height and clamps near 10.5 seconds; the roughly 3-second travel is newly designed, not dynamically verified. Initially C is inside, A one step outside, B east within a one-step thrust. Draft action safe area: x=0.12–0.88, y=0.10–0.78; candidate subtitle band y=0.82–0.94, rechecked against actual framing. No initial destruction; gate clamps spear at the end.

| Shot | Time/net duration | Action and result | Camera/generation and sound |
|---|---|---|---|
| M01 | 0–5 s / 5 s | C retreats left inside with box; A watches B's front hand. B steps into a thrust; A's right staff deflects tip north and retreats half a pace. Tip crosses former chest position without impact | Stable southern medium-wide, crossing central, door/C rear left; GEN_M01 centers one deflection, whoosh → wooden shafts contact → bootsteps |
| M02 | 5–10 s / 5 s | B recovers spear; A retreats along the corridor's south side to the gate lever, pulls with left hand, and turns sideways through door. B rushes in and extends spear to block the descending gate | Same-side medium, head/hands/lever readable. Multi-event SHOT split as M02a/b/c below; mechanism into footsteps |
| M03 | 10–15 s / 5 s | Gate clamps shaft with a narrow gap; B still grips and tries to pull it free. A retreats inside with staff guarding and leaves screen left with C | Read contact in a medium-close gap view, then slightly widen for result. GEN_M03 inherits half-lowered gate/inserted spear; clamp onset, gate vibration, shaft tug, footstep tails |

SHOT_M01/M02/M03 each have 5 net seconds, not three mandatory 5-second requests. Split M02 in advance: GEN_M02a selects 5–6.5 seconds, A reaching lever while B recovers; GEN_M02b selects 6.5–8 seconds, lever pull and withdrawal inside before B extends spear; GEN_M02c selects 8–10 seconds, B extending into the descending gap, not yet clamped at the end. M03 begins just before gate and spear meet. Total net runtime: 5 + 1.5 + 1.5 + 2 + 5 = 15 seconds. Fill request duration/handles from actual tools; short selections imply no corresponding supported input duration. Edit away repeated handles. Three shots are an editing design, not seamlessness; short-segment seams still need pilots. Static arithmetic does not prove actions fit.

M01 production-layer example: fixed layer records actual approved CHAR_A/B/C and GATE versions; scene layer places door left, attacker right, C already inside; action layer has B's one-step chest thrust and A's right-staff deflection/retreat; camera layer is stable south medium-wide with central contact; effects constraints: no powers, no hit flash, spear stays in B's two hands. This is a production card, not directly submit-ready prose. Actual input describes all three visible appearances and references only images actually uploaded, never internal IDs as character substitutes.

Opening/ending check: M01 ends with B's two hands on spear and A's staff still right-handed; M02 ends with A inside, spear in gap, gate descending; M03 ends with shaft jamming gate, B east, A/C west, no teleporting or restored gate. Static timing can be calculated; actual action/lip sync/listening await video validation.

## Retained 30-second action core: guard escorts a companion

A new design with provisional timing, neither a recreation of the four references nor a completed dynamic previs.

### Goals and constraints

A uses a short staff to escort box-carrying C through a gate; B seeks the box with a spear. A aims to close the gate and break pursuit, not win the fight. A's left shoulder is lightly injured throughout, staff always in the right hand. A deflection membrane at the staff tip survives one frontal crossing only and cannot return during this scene. It stays on the tip, never expanding into a body shield.

Look: clear cel shading, cool-gray stone, warm interior lamps, 2D key poses with a simple 3D set. A's short jacket/tied hair preserve weapon-hand visibility; B's spear is about one-and-a-half body heights, needing forward/back clearance. Light rain supplies wet-ground feedback only. The ability forms a narrow fan at the staff tip, not a full-screen flash.

### Space

Top view: west ← interior/escape | gate x=0 | A x=3 | B x=8 → east. C begins x=1 and withdraws west. Main corridor about 4 meters wide, no steps. Lever at the south end of the east-side doorframe; gate descent about 3 seconds. Shot 01 establishes open gate/control.

Camera mainly south: west is screen left, east right. A/C generally withdraw right-to-left, B follows. Brief northward flanking stays within the corridor; camera does not cross north. The same warm lamps and stone frame anchor inside/outside. B remains mobile after closure; only pursuit is blocked.

### Main storyboard

| Shot | Time/duration | Action and result | Shot size and camera | Rhythm and cut |
|---|---|---|---|---|
| S01 | 0–3 s / 3 s | A between C and B; C withdraws to gate, B approaches x=8 to x=6; gate/lever screen left | Southern medium-wide, slight lateral move retaining all three and frame | Establish goal/route; cut as B lowers spear tip |
| S02 | 3–5 s / 2 s | A sees C still outside, returns gaze to B's front spear hand; retains attack line | Stable medium-close A, C/door readable behind | One decision; A signals C onward, cut on B's lead-foot start |
| S03 | 5–8 s / 3 s | B steps x=6 to x=4.5, thrusting at A's chest; A at x=3 slightly turns staff, uses sole membrane to deflect tip north, retreats x=2.5; membrane breaks apart | Southern medium-wide follows retreat slightly, both hands/feet/tip intact | Fast approach, brief crossing accent, readable retreat; no freeze |
| S04 | 8–10 s / 2 s | A's right hand maintains staff-tip contact outside shaft then releases; left shoulder pain catches. B recovers spear; A has no membrane | Arms/upper-body close, include A's face, retain screen direction | Read cost/injury; cut along recovering shaft |
| S05 | 10–13 s / 3 s | B steps slightly north while recovering, tries to flank A; A retreats x=1.8 then half a pace north to block line; C crosses to x=-1 | Wider south view with all three and gate | Reestablish lateral relation; C crossing changes A's options |
| S06 | 13–16 s / 3 s | B thrusts again from x=3.8; A can now slip south, tip passing former chest position, while withdrawing west x=0.8; B advances x=2.2 | Medium-wide laterally follows A, retains passing tip/open route | Brief evasion, recovery after clearing attack line; no contact flash |
| S07 | 16–20 s / 4 s | B shortens grip to withdraw spear. A continues retreating along the corridor's south side to the doorframe, deflects B's renewed probing shaft with staff, then releases. Left hand nears lever, right keeps staff | Low southern medium follows retreat then settles, frame/lever enter | One defense gains operation window; small left-arm movement preserves injury |
| S08 | 20–23 s / 3 s | A pulls low lever left-handed, face contracts with shoulder pain. Gate descends; A immediately turns sideways inside x=-0.8. B reaches x=1.5, spear extended to block gate | Door-side medium-wide includes control, A's exit path, descending gate | Operation → withdrawal → pursuit continuously; cut as spear enters gap |
| S09 | 23–26 s / 3 s | Gate clamps front shaft; B cannot pull it free. A retreats x=-1.5 with guarding staff. Gate stops above bottom with a narrow person-blocking gap | Gap/contact close, then slight same-shot widening to A; frame direction retained | Brief wood compression/metal vibration, then struggling; no declaration of B's defeat/death |
| S10 | 26–30 s / 4 s | Inside, A checks gap/B blocked, turns and withdraws west with C. Left shoulder low, membrane unrestored; B keeps pulling beyond gate | Interior southern medium-wide, departure left, gate rear right | Breath/steps lead, retaining blocked-pursuit result and pressure |

S08 descent begins after 20 seconds and clamps near S09's opening; refine exact timing in previs. S09 uses contact deformation/tugging to convey obstruction, not 3 seconds on one still. S07 deflection is ordinary direction/leverage defense, never a secretly restored membrane.

### Performance and visual supplement

| Shots | Performance/sound proposal | Effects and handoff |
|---|---|---|
| S01–02 | A quietly says "Through the gate first," checks C, then watches enemy; B advances silently | Normal light rain L0; hands, control, routes readable |
| S03–04 | A exhales briefly at collision, then contains shoulder pain; B looks to vanished membrane | Membrane L2 at tip only, deflection north; short fracture lines at contact, wet prints persist |
| S05–06 | A sidesteps only after confirming C inside; expression shifts from pressure to focus | Evasion L1: local splash/short spear-tip trail only, no hit sparks |
| S07–08 | A does not explain tactics; mouth briefly tightens on left-hand operation. B pursues on seeing gate | Ordinary staff/spear contact L1; mechanical descent, no new ability |
| S09–10 | B's shaft tug and gate vibration; A breathes fast, turns without swinging injured shoulder | Gate/spear L2 uses deformation, a little wood debris, vibration; gap/clamped spear persist |

A sound proposal, not recorded or listened to. One brief line here does not require taciturn characters elsewhere.

### Minimum assets and pending acceptance

- A: tied hair/short jacket, right staff, restricted left shoulder; check staff turns, side slips, low left-hand operation, sideways doorway passage.
- B: spear-tip contact/clamp deformation, two-handed grip-spacing changes; check no ground/frame penetration.
- C: box-carrying withdrawal, stays inside after crossing rather than teleporting back to combat.
- Set: corridor white model, open/descending/jammed gate states, control, interior lamps, wet-ground responses.
- Dynamic previs must confirm whether S07 fits deflection plus control approach within 4 seconds, S08 allows operation/withdrawal, and clamped gap really blocks a person. If not, simplify action or adjust segmentation first, keeping 30 seconds total; do not hide failures with fast cutting.

## Transfer across genres

Keep "goal → constraint → choice → consequence," rewriting mechanics rather than changing skins only.

- Realistic combat without powers: remove membrane and recheck whether weapons/bodies can deflect the attack; a short staff cannot still magically redirect every heavy blow.
- Mecha withdrawal: replace shoulder restriction with a failed actuator and rebuild gate scale/clamp strength accordingly. Cockpit acting corresponds to external machine state.
- Exaggerated comedy: a shaft may bend and load, with delayed enemy response, but establish recoverable-deformation rules first. The outcome still blocks an exit or changes pursuit.

## AI video prompt adaptation as needed

Use generation handoff to establish platform operation and real assets first. Specify reference responsibilities only for provided images; without them, describe self-contained appearances. Check independent events, opening/ending support, and observable acceptance per generation segment. Storyboard shots and generation segments need not map one-to-one; complex-contact splits retain matchable poses. Both 15/30-second cases are untested designs, not platform-tested plans exempt from current handoff.

Usable structure: `Fixed identity and weapon hands → Current space/carried pose → One main attack/defense and result → Camera task → Performance → Style/effects constraints → Ending posture/environment state`.

For example, adapting S06 includes "C already inside; A has no membrane; A evades the chest-high thrust south while retreating west; the spear crosses the old position; no hit flash." Retain only high-risk negative constraints. Without a specified platform, invent no parameters, duration limits, or capability guarantees.

## Parallel non-action minimum case: 30-second tea-room standoff

An original design, not generation-validated, presented alongside the original 30-second gate core; it does not establish validation across every genre. Show these shots only for an explicit structural request; default actual input is plain prose.

| Narrative timing | Scene organization | Sound and meaning |
|---|---|---|
| First ~8 s | Two-shot establishes door/table/wet envelope; visitor places letter beside cup | Dripping threshold, quiet room; evidence enters |
| Middle ~8 s | Doorkeeper looks at letter: "Which road did you take back?" Visitor looks at doorway, answers "The bridge is down." | Reaction room after short lines, no added inner narration |
| Next ~8 s | Medium-close holds one stopped hand; doorkeeper moves cup beside letter, yielding doorway route | Cup base touches table; action shows whether passage is granted |
| Final ~6 s | Return two-shot; visitor withdraws hand and rises, rain outside grows nearer | Retain unfinished relationship, no new pursuers |

Connect structure to [narrative structure](../narrative/story-and-scene.md), shots to [dialogue scenes](../narrative/story-and-scene.md), and breathing room to [atmosphere/ritual](../narrative/story-and-scene.md). 30 seconds is an editing goal; actual request durations follow the platform. The table is neither four generations nor four event units. Use established project appearance cards, submit self-contained segments, and route sound by current native capability.









