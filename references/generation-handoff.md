# Generation Handoff

Turns the design into inputs a platform can actually run. v3 keeps v1's conditions-first discipline and drops its budget-as-law.

## 1. Minimum conditions (ask once, together)

`Platform and model (unknown is fine) | requested clip length | one generation or several clips edited together | reference images that will really be uploaded (character, scene, effect) | first or last frame used | native audio and native speech supported and wanted | actions and results that must survive`

- Use what is known. Ask only what changes the plan; continue working while you wait.
- Separate **creative gaps** from **technical gaps**. Unknown model: write a platform-neutral Extended draft with assumptions listed. Unknown story: discuss the story first.
- A feature is "supported" only if the user confirmed it or you checked current official docs. A product name does not confirm the underlying model or version.

## 2. Branch by actual inputs

| Input | How to write |
|---|---|
| No reference images, no first frame | The prompt carries identity in words (slot 2: face structure, one asymmetry, skin, hair, costume, weapon or prop). Never write "use the approved image" or "continue from the last frame" when there is none |
| Character or ability images, no first frame | Say what each file is for in the control notes; keep the text anchors anyway; do not claim a first frame is locked |
| A first frame | Check left and right, support, hands, damage, and light against the design; if the frame is wrong, fix it first. Describe the motion that follows, not the frame again |
| Last frame | Use only if it is actually supplied; describe how the motion arrives |
| Several reference types (image, video, audio) | Record in notes what each is used for (identity, motion, scene, voice); text anchors remain |

Reference IDs and asset names are for management. If the platform does not carry context, the prompt must describe visibly; never an ID alone.

## 3. Clip splitting (Tier A)

### Event boundaries

An event is one causal interaction: a directed attack/threat, control attempt or transfer, the response to it, and its immediate result. Identify the initiator, target, required response and resulting relationship. Do not count verbs or call an entire fight one exchange.

- Approach, a sidestep, a parry and recovery belong to the same interaction when they realize or answer the same threat. They still consume runtime and contact complexity.
- A counterattack that creates a new threat starts another interaction even without a pause. A renewed thrust after an evasion is another; independent simultaneous attacks are separate interactions even when one motion answers both.
- A sustained bind or push can remain one interaction while the same control relationship continues. A new disarm attempt, changed target or independent threat starts another. Minor grip adjustments alone do not.
- Record a lasting result once: a strike and its directly caused knockdown are one interaction with a persistent result. An independent door closure, transfer or environmental collapse is a separate state transition. Trace dependencies rather than double-counting the same consequence.

| Sequence | Working decomposition |
|---|---|
| Thrust, sidestep clear, counter, retreat clear, renewed thrust | Three interactions: thrust/evasion, counter/retreat, renewed thrust and its response; not five verbs or one whole exchange |
| Blade bind maintained while both circle | One sustained interaction if control is unchanged; time and support still need checking |
| Block a downward blade while a second attacker thrusts | Two independent threats, with their separate response demands, even if simultaneous |
| Strike knocks the target down; a door then shuts independently | One strike interaction with knockdown result, plus one separate door transition |

This is a design convention, not a calibrated measure of model difficulty. Rhythm examples in [action modes](action-modes.md) use these interaction starts. One event is neither one shot nor one generation request. For natural-language prompting, keep these labels in the internal design record.

### Capacity and grouping

- **Rhythm and request capacity differ.** The action mode suggests pacing; its density examples are estimates, not quotas or platform limits. Check the actual runtime, contact complexity, available assets and verified model behavior. Mark untested combinations as untested.
- **Candidate grouping by mode:** consider exchange pairs for a duel, continuous pressure with carried stamina for a last stand, approach and strike together for stealth, burst/aftermath boundaries for ambush, teaching beats for sparring, and terrain segments for pursuit. These are possible joins, not mandatory cuts or request counts.
- **Recheck** at a new attack, changed defensive relationship, complex contact or camera task. Keep distinct events visible and test whether their timing, support, hands, consequences and recovery fit together. Re-stage, adjust timing/camera, or split when demands cannot coexist. Successive shots in a supported multi-shot request are not automatically separate requests; extra runtime does not erase event complexity.
- **Long takes:** one continuous evasion can remain one shot or request when its motion and timing fit. Independent threats remain separate events in the design even when a single movement avoids them; writing "continuous take" does not establish capacity.
- **Dialogue scenes** split by conversation unit (`dialogue/conversation-units.md`), not by event count.
- **Pilot when useful:** recommend testing a principal interaction or landing before costly batch generation; do not withhold a requested complete draft or reduce continuous-action ambition because capability is unknown. Generation still requires actual tools, inputs and authorization.
- **Bridges:** backward to forward needs braking and thrust; mid-air direction change needs an ability or momentum reason; a beam breaking under a hanging load needs a stated force path.

## 4. Multi-shot and long models

For a platform that accepts several shots in one prompt, write the look anchor and subject lock once, then run the shots in prose with cut language. Verify per model (`models/README.md`, item 2). Continuity inside one pass is the model's job: restate identity and spatial anchors once and inspect the result. Seams between passes still apply.

## 5. Native audio and speech

Native sound effects, native dialogue, and lip sync are three separate things; none implies another. v3's default is lines **inline** in the prompt as quoted speech with delivery. If native speech is unverified, still deliver the lines inline (they give mouth timing) plus a voice script outside the block, and say that sync is untested. Never claim sync.

## 6. Platform adaptation

Core intent and locked facts do not change. Adjust syntax, control parameters, prompt length, and the negative field to the platform. Weights, brackets, and reference tags are platform-specific syntax; no universal form exists. Do not extend one brand's features to all versions. If capabilities are unverified, deliver the neutral draft and say so in plain language.

## 7. Seam state (carry between clips)

Position (x, y, z) and facing, anchor, support and posture, held objects, injury and stamina, ability state, environment state, plus light direction and prop state. Dialogue scenes carry each person's anchor, orientation, posture/height, distance, routes/access and any unresolved approach, invitation or refusal from the [unit spatial spine](../dialogue/spatial-blocking.md). Preserve deliberate holds too; a routine walk or turn is not automatically another request. Write them as the next clip's opening facts.

## 8. When the platform forces a downgrade

The goal is kept; the plan changes. Say what changed and which specific load conflict it solves. A user-demanded core effect (a named move, a face target) is never replaced without options and the user's choice. If the user insists on the original, deliver it labeled "to test".

## 9. A "ready-to-submit test prompt"

Only when the conditions and assets are real, the Tier A check is done, the text does not depend on missing references, and key events have observable acceptance checks. This status means organized input, not a working clip.

## 10. Delivery choice

Reuse the user's choice of complete text or a test segment. An explicit full-draft request authorizes full text delivery; a staged exploration request keeps its chosen sequence. Ask only when this choice is genuinely unresolved and affects delivery. Text delivery and generation request length are separate decisions. Recommend a pilot for untested complexity without withholding requested text or spending on generation without authorization.
