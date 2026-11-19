# v3 Extended Examples

Three illustrative Extended prompts. **None has been run on a video model.** Characters, props, and facts are invented for the examples and do not transfer to any project. Each copy block passes `scripts/lint_prompt.py`.

## Example 1: Power dialogue (English)

**Inputs from the user:** An office study, late afternoon. Chen is Wu's superior. Wu reports that a shipment failed customs. Chen should not raise his voice. Outcome: Wu finishes his sentence steadily; Chen lets him.

**Profile:** situation A (seated formal) | Purpose: expose a failure and test composure | Power: Chen high, Wu low | Audience: none | End mode: hold.

**Design record (internal, not in the prompt):**
- Locked: Chen superior, Wu subordinate; shipment failed customs on Tuesday; Chen stays calm; Wu ends steady.
- Added texture: porcelain cup and saucer for Chen; tungsten desk lamp; window light; dust in the beam.
- Status ledger: Chen high, Wu low. Chen widens the gap with silence. Wu makes a small claim at the end.
- Dialogue: Wu's stammer is anxiety; Chen's echo "Tuesday." is the pressure move.
- Beats: see `lens/body-and-status.md` section 9.

**Copy block (Extended):**

> Live-action drama, 16:9. Shot on a 85 mm lens with shallow depth of field, 35 mm film character with fine grain, warm tungsten palette and deep, dense shadows, natural motion blur, locked-off with one slow push-in.
>
> Chen is in his mid-fifties, heavy-lidded, with grey stubble that thins along the cheekbones; deep lines run from his nose to the corners of his mouth, and the skin under his eyes is slightly dark, with one faint blue vein. His left brow sits a little higher than his right. He wears a charcoal wool jacket, rubbed pale at the cuffs where his forearms rest, and a white shirt with a collar that has softened with washing. Wu is in his early thirties, narrow-faced, with a faint flush rising along his neck, short black hair with a few strands lifting at the crown, a grey suit creased across the lap, and thin fingers with ridged nails.
>
> A study at late afternoon: a heavy desk, a worn leather armchair, a wooden visitor's chair, shelves of ledgers. A low tungsten desk lamp throws amber light across Wu's lower face from the left, its steep falloff dropping his right cheek into shadow; cool grey window light behind Chen rims his silver hair, and a small window-shaped highlight shows in each of his eyes. Dust turns slowly in the window beam.
>
> Chen sits far back in the armchair, right ankle over left knee, a porcelain cup balanced on his knee. Wu perches on the front third of the wooden chair, palms flat on his thighs. Wu swallows, then says, voice thin and fast, "Sir, the shipment, it, uh, it didn't clear customs on Tuesday." Chen says nothing. His thumb turns the cup a quarter-turn on its saucer. Wu's left hand slides to his cuff and tugs. The camera begins its slow push-in on Chen's face. Chen lifts the cup, the lid ticks once against the porcelain, and he sips with his eyes on Wu over the rim, his expression flat and patient. He sets the cup down with a small click and lets the silence run. "Tuesday," he says, low and unhurried, his voice falling at the end. A thread of steam bends toward Wu. For an instant one corner of Chen's mouth tightens and lifts, then his face goes blank again. Wu's palms stay flat; he takes one slow breath through his nose and says, level, "Tuesday. Yes, sir. The paperwork was filed late, and I should have caught it." Chen's ankle changes sides; the lamp light slides along his polished shoe.
>
> The room is quiet except for the tick of the cup and a distant clock; Chen's voice sits low and dry, Wu's a little breathy. The shot ends on the two of them in the same chairs, Chen's cup half empty on his knee, Wu's palms flat on his thighs, the lamp's amber on Wu's chin and the grey window light on Chen's hair.

**Added-texture note (outside the block):** Added: porcelain cup and saucer, tungsten desk lamp, window light with dust, wool jacket details, and Wu's cuff tug as his self-touch. Assumptions: modern workplace and period unspecified; no native speech verified (voice script below).

**Voice script (outside the block):**
```
Speaker | Line | Delivery | Pause
Wu | "Sir, the shipment, it, uh, it didn't clear customs on Tuesday." | thin, fast, a stammer on "it" | 0.3 before
Chen | "Tuesday." | low, unhurried, falling | 0.8 before
Wu | "Tuesday. Yes, sir. The paperwork was filed late, and I should have caught it." | level, a short inhale first | 1.0 before
```
*Pauses are estimates; read aloud before relying on them.*

**What the lint sees:** a few modal words ("should have caught it") appear inside a quoted line and are fine.

## Example 2: Action with a seam (translated example)

**Inputs:** A snowy night at an old tower door. Lin guards the entrance with a short staff; Han carries a spear. Lin has a concealed left-forearm injury. Han thrusts, Lin parries and closes, and Han gives half a step. Neither wins.

**Context Profile:** Duel: a doorway stalemate with one person concealing an injury. End-state: hold. A last-stand version would need different rhythm (see case 2 in `context-routing-examples.md`).

**Internal design:** Locked: Lin's left-forearm injury, staff, spear and unresolved result. Added texture: snow, breath fog, a doorway lantern and staff patina. Tier A: thrust -> parry -> close -> retreat in one contact chain. Tier B: Lin hides her left hand in her sleeve and breathes shallowly; Han watches her cuff. Tier C: amber lantern light, cold blue ambient, coarse grain and a narrow-shutter feel.

**Copyable prose (Extended):**

> Photoreal cinematic imagery, 16:9. A 35 mm lens with handheld operator breath, crisp narrow-shutter motion and medium 35 mm film grain. Faint halation surrounds the lantern; cold blue and amber dominate, with dense shadows retaining coarse fabric texture.
>
> Lin is in her early thirties, narrow-faced, with the right brow slightly higher. Cold reddens her nose tip and ear rims; her lips are cracked with a small split at the left corner. Short hair is tied behind her head, stray strands lifting in the wind. Her old grey padded jacket has flattened quilting at the elbows and a long left cuff worn pale by her hand. Her right hand grips a short iron-tipped wooden staff, its grain polished by her palm. Han is about forty and tall, with coarse grey-flecked jaw stubble and an old mark under one eye. Snow gathers on the shoulders of his grey travel coat. He holds a long spear in both hands; its dark shaft has darkened further where it is gripped and its point carries a thin film of oil.
>
> Thin snow covers the old tower steps at night. A lantern beside the frame lights the threshold and Lin's right cheek amber against the cold blue snowfall. Flakes slant through its light and each exhale leaves a pale cloud. A cross-draft bends the flame slightly left, gently shifting its shadows. A small lantern-shaped catchlight sits in Lin's eyes.
>
> Lin stands inside the doorway with weight on her right leg, her left hand withdrawn into her sleeve and the short staff resting diagonally on her right shoulder. Her breathing stays shallow and even. Han waits a spear length away, watching her left sleeve, his spear lowered and his exhale drawn long in the cold. He lifts the point a small fraction, then thrusts straight at her chest. Lin brings her right-hand staff across the shaft and sweeps left; the point slides past where her chest had been. With the staff head pinning the shaft, she steps forward on her right foot and drives the staff and right shoulder into Han's chest. His chest compresses first; then he yields half a step, steadies on slightly bent knees and draws the spear back. The camera follows Lin's step in a small push, settling at contact as snow crosses the foreground. Lin stops with her left arm still hidden, staff in her right hand and the same shallow, even breath.
>
> Snow lands softly on the stone steps. Staff and spear shaft meet with a short dull knock, and the lantern cord lightly taps the frame in the draft. The final frame holds Lin inside the open door and Han a spear length away with his weapon recovered. Snow continues between them while amber lantern light gently moves over Lin's cheek.

**Notes outside the block:** Added: lantern, breath fog, staff patina and snow. Native audio capability is unverified.

## Example 3: Face close-up (English, protect the user target)

**Inputs:** The user demands a close-up of Lin hiding fear when Han names her wound.

**Profile:** display rules: among enemies, strong mask | shot: close | End mode: hold.

**Design (internal):** Mask: calm and level. Leak: one swallow and a flicker at the brows. Keep the fight out of this clip.

> Live-action drama, 16:9. Shot on an 85 mm lens with shallow depth of field, 35 mm film character with fine grain, a faint halation around the lantern's flame, cool blue ambient with a warm amber edge, dense shadows that keep the weave of her collar, locked-off with a very slow push-in.
>
> Lin is in her early thirties, narrow-faced, her right brow set a little higher than her left, short black hair tied back with a few strands loosened by wind and beaded with melting snow; fine lines gather at the corners of her eyes, a faint blue vein shows under the lower lid, and the cold has reddened the tip of her nose and the rim of each ear, which glow faintly warm where the lantern catches them. Her lips are dry, with a small split at one corner. She wears a grey padded jacket with the collar rubbed pale, snow melting into dark spots on the shoulder.
>
> Han stands just out of focus in the foreground, the edge of his grey travel coat and a hand gripping a spear shaft softly blurred, and the stone doorway behind Lin shows a worn threshold under a thin layer of snow. Snow falls through cold blue air; a lantern at the camera's right throws a warm edge across her cheek and jaw, its flame leaning slightly in the draft, and a small lantern-shaped highlight sits in each of her eyes. Each exhale leaves a pale puff in front of her face.
>
> She looks at Han's face, her expression level, her breath shallow and even. When Han says, low and steady, "Lin, your left forearm is wounded," her upper lids lift a hair and her brows draw together for an instant; her lips press into a thin line, her throat moves in one swallow, and a pulse ticks at her neck. Then her face smooths into a calm, patient blankness, and her eyes drop for a moment to Han's hands before returning to his face. The camera's push-in has barely moved as his words trail off, and a snowflake lands on her lashes and melts. Her gaze holds steady on him.
>
> The night is quiet except for the soft tick of snow on stone and the faint creak of the lantern's cord. The shot ends on Lin's face holding still, the lantern's amber on her cheek, the cold blue behind her, and a single snowflake settling on her shoulder.

**Why the face beat is one flicker plus a mask:** a single small leak (brows and swallow) keeps the beat readable; a stack of leaks would blur. If the model cannot render the flicker, fall back to gaze and head turn (`lens/face-pass.md` section 7).

## Before and after: the v1 problem

**v1-style output (analytical):** "A and B face each other. A, the superior, shows composure through a calm, unhurried posture; there is tension between them. A does not interrupt and does not move. Only after B finishes speaking does A respond. No new action is added in this clip."

**v3 output (execution):** see Example 1. The superior sits back, ankle on knee, cup balanced; the cup turns, lifts, ticks, and lands; his silence runs; the subordinate perches and swallows. Every sentence is something a camera or microphone would capture.

## Compact tier (same scene, for "short/lite")

> Live-action drama, 85 mm, shallow depth of field, warm tungsten, fine grain. Chen, mid-fifties, grey stubble, charcoal jacket, sits far back in a leather armchair, ankle over knee, a porcelain cup on his knee; Wu, early thirties, grey suit, perches on the front of a wooden chair, palms on his thighs. Wu says, thin and fast, "Sir, the shipment, it, uh, it didn't clear customs on Tuesday." Chen lifts the cup, sips with his eyes on Wu, sets it down with a click, and says low, "Tuesday." Warm lamp on Wu's chin, grey window light on Chen's hair. The shot ends on both still in their seats.

## Fixed-camera defense: short output, complete design

User facts: a guard with a short staff holds a narrow doorway against a spear thrust, redirects it, and keeps the doorway. No injury or winner is added. Spatial record: guard inside threshold, attacker outside at spear reach; the guard remains planted, spear is redirected outside the opening. This is a design example, not a model test.

> A fixed medium-wide view holds the doorway and both fighters. The guard braces his rear foot against the threshold, his short staff across his body. The attacker thrusts the spear at his chest. The guard catches the shaft with the staff and turns it toward the outer doorpost; his shoulders yield with the pressure while his feet keep their place. The spear point passes outside the opening. The attacker draws it back; the guard restores the staff across the doorway. Wood knocks against wood, then the scrape of the spear shaft fades.

Coverage: attack, contact, redirection, recovery and continued guarding are visible. No camera orbit, height change or anchor change is needed. In a pursuit or open duel, the same toolkit may instead support extensive travel; do not transfer this hold to every fight.

