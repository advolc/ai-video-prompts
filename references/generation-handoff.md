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

- **Main interaction:** one exchange of attack, defense, or transfer with a clear outcome.
- **Guideline:** about 3 independent interactions per ~5 s of runtime. This calibrates to short clips on current-generation models; scale after testing at your real duration.
- **Split** when a clip contains a new attack, a changed defensive relationship, a new complex contact, or a second camera task. A longer duration does not make several exchanges into one.
- **Long takes:** a dodge of one wave with no complex contact can remain one long unit, if the prompt says it is one continuous take.
- **Dialogue scenes** split by conversation unit (`dialogue/conversation-units.md`), not by event count.
- **Test first:** when complex contact is unverified, generate one main exchange or one landing before committing to the whole sequence.
- **Bridges:** backward to forward needs braking and thrust; mid-air direction change needs an ability or momentum reason; a beam breaking under a hanging load needs a stated force path.

## 4. Multi-shot and long models

For a platform that accepts several shots in one prompt, write the look anchor and subject lock once, then run the shots in prose with cut language. Verify per model (`models/README.md`, item 2). Continuity inside one pass is the model's job: restate identity and spatial anchors once and inspect the result. Seams between passes still apply.

## 5. Native audio and speech

Native sound effects, native dialogue, and lip sync are three separate things; none implies another. v3's default is lines **inline** in the prompt as quoted speech with delivery. If native speech is unverified, still deliver the lines inline (they give mouth timing) plus a voice script outside the block, and say that sync is untested. Never claim sync.

## 6. Platform adaptation

Core intent and locked facts do not change. Adjust syntax, control parameters, prompt length, and the negative field to the platform. Weights, brackets, and reference tags are platform-specific syntax; no universal form exists. Do not extend one brand's features to all versions. If capabilities are unverified, deliver the neutral draft and say so in plain language.

## 7. Seam state (carry between clips)

Position and facing, support and posture, held objects, injury and stamina, ability state, environment state, plus light direction, prop state, and distance for dialogue scenes. Write them as the next clip's opening facts.

## 8. When the platform forces a downgrade

The goal is kept; the plan changes. Say what changed and which specific load conflict it solves. A user-demanded core effect (a named move, a face target) is never replaced without options and the user's choice. If the user insists on the original, deliver it labeled "to test".

## 9. A "ready-to-submit test prompt"

Only when the conditions and assets are real, the Tier A check is done, the text does not depend on missing references, and key events have observable acceptance checks. This status means organized input, not a working clip.
