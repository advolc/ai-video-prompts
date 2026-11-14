# Delivery and QA

Replaces v1's anti-lazy protocol. v1 spent its energy preventing over-reach and ended up suppressing richness. v3 keeps what protects the user (the story stays theirs; claims stay honest) and moves enrichment into the Lens layer (`lens/lens-layer.md`).

## 1. What the user receives

1. **The copy block:** one prompt per clip, plain prose, Extended by default (`lens/output-skeletons.md`). Nothing in it is a label, a module name, or a design term.
2. **Outside the copy block** (short, plain):
   - *Added texture:* one line listing notable additions (props, business, light, optics) so the user can veto.
   - *Assumptions:* anything inferred (model, duration, era, etiquette).
   - *Voice script,* when the platform lacks native speech or the user will voice in post.
   - *What to test first,* if one contact or one face beat is the riskiest.
3. **Engineering view** (ledgers, tables, seams): only when the user asks. Do not bundle both versions.

If the user only wants the prompt, deliver the prompt and the added-texture line.

## 2. Creative boundary (kept from v1)

The story belongs to the user. Plot, outcome, who wins, character identity, locked objects, world rules, and anything the user named are not yours to write. When the idea is missing, offer 2–3 short options, let the user choose, then ask only what changes people or endings. A request like "30-second fight, this art style" is not yet a story. When the user says "you decide", decide inside that scope and mark it as delegated. When the user says an earlier version overreached, restore the last confirmed state and drop everything that depended on the invented part.

## 3. Script to prompt

A literary script or description is not a prompt. Convert it into visible, time-ordered physical events and then run the Lens procedure (`lens/lens-layer.md` section 5). Keep the intent; poetic images become what can be seen. Optionally keep one line outside the block that records the original image.

## 4. Red lines for the final text (all enforced by `scripts/lint_prompt.py` where a pattern can catch them)

1. **No production scaffolding.** No clip IDs, time-range labels, "must-do", "ambient", "seam", "same as before", "see above". Carry-over is written as present-tense facts.
2. **No negations or constraints as sentences.** State what is there. A negative field on a verified platform may hold at most two short exclusions.
3. **No explanation, theory words, or evaluation.** Show the cause as behavior.
4. **Action reads as one connected chain** using temporal connectives (as, then, when, a beat later), not conditionals. Movement through space is written as **paths** (shape plus landmark or opponent-relative direction), not only as steps in and back.
5. **Self-contained.** The first sentences carry the look and every present character's recognizable look. Never only a name, "the one in red", or "as before".
6. **Honest.** No claim that the clip was generated, tested, or lip-synced unless it was.

## 5. Delivery preference

Ask once, if unknown: all prompts now, or one trial clip first? Reuse the answer. Never withhold later clips pending the first. A long project that is long deserves a complete file, not just the first clip.

## 6. Pre-delivery self-check

1. Is the story still the user's? Locked facts unchanged?
2. Does every prompt pass the lint and the coherence checklist?
3. Is each prompt Extended (unless asked or forced otherwise) and does it fit the model's limit?
4. Does each clip pass Tier A (about 3 independent interactions per ~5 s, contact before consequence, support and recovery)?
5. Are all five passes visible in the text where the shot size allows (optics, light, skin, face, body)?
6. Does dialogue appear as spoken-register lines with delivery, fitted to the clip length?
7. Are body beats anchored, status readable, props consistent?
8. Does each clip's opening state equal the previous clip's end state?
9. Is the added-texture note written, and are assumptions labeled?
10. Verified, assumed, untested: labeled correctly, no result promises?
11. **Spatial gate** (any fight): is there an arena card and a position ledger? Does `python scripts/check_spatial.py ledger.json` pass for the mode (line-lock run, lateral deviation, bearing sweep and coverage, level change, anchors, plant-and-absorb share)? Does every defensive response include a displacement?
12. **Linear-verb check:** does `lint_prompt.py` report more linear moves (steps in or back, retreats) than spatial ones (circle, slip, pass, level change, push-off)? Does the camera use at least two axes relative to the duel line?

## 7. When a clip fails

Label the failure type: identity, space (including **spatial-linear**: a fight confined to one line), action, contact, light/optics, face, body, speech, sound. Find the **earliest** wrong point; check what depends on it. Fix by removing competing tasks, tightening the contact chain, or changing the look anchor; do not pile on adjectives. Without actual output, do not claim a model "cannot" do something. Record results in `models/` (`evals/cases.md` has a template).

## 8. Honest status language

| Use | Meaning |
|---|---|
| Verified | Official docs or the user confirmed it this session |
| Assumed | Inferred; flagged |
| Untested | Written, never generated |
| Tested | A clip was generated; say what happened |
