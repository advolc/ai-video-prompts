# Delivery and QA

Replaces v1's anti-lazy protocol. v1 spent its energy preventing over-reach and ended up suppressing richness. v3 keeps what protects the user (the story stays theirs; claims stay honest) and moves enrichment into the Lens layer (`lens/lens-layer.md`).

## 1. What the user receives

1. **The copy block:** one prompt per clip, plain prose, Extended by default (`lens/output-skeletons.md`). Keep analytical scaffolding outside it; verified platform syntax and quoted speech retain their needed form.
2. **Outside the copy block** (short, plain):
   - *Added texture:* one line listing notable additions (props, business, light, optics) so the user can veto.
   - *Assumptions:* anything inferred (model, duration, era, etiquette).
   - *Voice script,* when the platform lacks native speech or the user will voice in post.
   - *What to test first,* if one contact or one face beat is the riskiest.
3. **Engineering view** (ledgers, tables, seams): only when the user asks. Do not bundle both versions.

If the user only wants the prompt, deliver the prompt and the added-texture line.

## 2. Creative boundary (kept from v1)

The story belongs to the user. Plot, outcome, who wins, character identity, locked objects, world rules, and anything the user named are not yours to write. When the idea is missing, follow the chosen exploration workflow in `ux/interaction.md`: gradual dimensions by default, complete directions when requested. A request like "30-second fight, this art style" is not yet a story. When the user says "you decide", decide inside that scope and mark it as delegated. When the user says an earlier version overreached, restore the last confirmed state and drop everything that depended on the invented part.

## 3. Script to prompt

A literary script or description is not a prompt. Convert it into visible, time-ordered physical events and then run the Lens procedure (`lens/lens-layer.md` section 5). Keep the intent; poetic images become what can be seen. Optionally keep one line outside the block that records the original image.

## 4. Red lines for the final text (reviewed with `scripts/lint_prompt.py`; patterns do not establish semantic compliance)

1. **No production scaffolding.** Avoid internal IDs, unresolved cross-references and analytical labels. Ordinary words, exact speech and verified platform syntax are exempt. Carry-over is written as present-tense facts.
2. **Prefer direct depiction.** Preserve dialogue wording and meaningful ordinary usage; use a negative field or structured syntax according to verified platform behavior, without an arbitrary exclusion count.
3. **Translate analytical notes into behavior.** Retain brief context when it aids interpretation and preserve exact spoken lines.
4. **Action reads as one connected chain** using temporal connectives (as, then, when, a beat later), with clear order. Describe paths or purposeful holds using landmarks or opponent-relative directions; steps in and back are valid when sufficient.
5. **Self-contained.** Supply necessary identity and spatial anchors in text or actual provided reference inputs. Do not rely on missing assets or unresolved "as before" references.
6. **Honest.** No claim that the clip was generated, tested, or lip-synced unless it was.

## 5. Delivery preference

Use the delivery choice in `generation-handoff.md` section 10; reuse explicit scope and ask only if unresolved. Never withhold later clips pending the first. A long project that is long deserves a complete file, not just the first clip.

## 6. Pre-delivery self-check

1. Is the story still the user's? Locked facts unchanged?
2. Does every prompt pass the lint and the coherence checklist?
3. Is the prompt sufficiently developed for its purpose, at the requested length and within actual limits?
4. Does each request pass the capacity-and-splitting check in `generation-handoff.md` section 3: timing and simultaneous demands fit, distinct events remain visible, and contact, support, consequences and recovery are readable? Does the selected mode serve this scene rather than a numerical quota?
5. Are relevant optics, light, material, face and body details selected for the actual shot, without requiring every pass to appear?
6. Does dialogue appear as spoken-register lines with delivery, fitted to the clip length?
7. Are body beats anchored, status readable, props consistent?
8. Does each clip's opening state equal the previous clip's end state?
9. Is the added-texture note written, and are assumptions labeled?
10. Verified, assumed, untested: labeled correctly, no result promises?
11. **Spatial integrity:** do positions, support, paths or purposeful holds serve the scene and remain continuous? Use a concise record for simple exchanges, expanded coordinates for complex ones. Numeric diagnostics validate data and explicit project targets only.
12. **Movement and camera:** are explicit travel/hold and framing targets preserved? A fixed camera or linear defense may be correct; movement-word counts and axis variety are not acceptance quotas.

13. **Dialogue spatial decision gate** (including silent interaction): apply [dialogue spatial blocking](../dialogue/spatial-blocking.md) section 6 to each unit. Check opening geometry, cue/goal, maintain/relocate/mixed choice, physically feasible path or concrete hold reason, counterpart response, ending relation/consequence, and seam. A motivated seated scene passes; decorative pacing and camera-only movement do not. This is a semantic/manual check, not a word-count test; fight displacement and axis thresholds do not apply.

## 7. When a clip fails

Label the failure type: identity, space (including a required movement that is missing or an incoherent path), dialogue-spatial-flat / dialogue-spatial-busywork / dialogue-spatial-jump (see `dialogue/spatial-blocking.md`), action, contact, light/optics, face, body, speech, sound. Find the **earliest** wrong point; check what depends on it. Fix by removing competing tasks, tightening the contact chain, or changing the look anchor; do not pile on adjectives. Without actual output, do not claim a model "cannot" do something. Record results in `models/` (`evals/cases.md` has a template).

## 8. Honest status language

| Use | Meaning |
|---|---|
| Verified | Official docs or the user confirmed it this session |
| Assumed | Inferred; flagged |
| Untested | Written, never generated |
| Tested | A clip was generated; say what happened |

## 9. Target coverage before style polish

Check each explicit action, spoken line, reveal, outcome and continuation fact against the actual delivered text. A described reaction does not substitute for its required trigger. Verify contact paths, listener response and end state. Formatting checks cannot establish coverage. Preserve meaningful dialogue words and verified platform syntax even if a textual heuristic flags them.
