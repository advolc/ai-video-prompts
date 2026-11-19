# Evals: find out what actually works

v3 has not been benchmarked. These cases are how you find out. Your own test of v1 against v2 was the first evidence either design had; this harness makes that repeatable.

## Protocol

For each case, run **Arm A** (your current best prompt, or the v1 output) and **Arm B** (the v3 Extended output). Generate at least 3 clips per arm on your target model. Score blind if you can (someone else shuffles the clips). Record results in `evals/results.md` using the template below.

## Cases

| # | Case | Stresses |
|---|---|---|
| 1 | One-on-one sword duel, incoming attack/parry then counter (two causal interactions) | Contact, support, consequence |
| 2 | Long weapon vs short weapon, close-in | Weapon logic, distance |
| 3 | Same fight, second clip, after a stagger and a dropped weapon | Seams and state carry-over |
| 4 | Two characters, a soft threat across a table, no fight | Status, listening, prop business |
| 5 | A character hides a wound while talking | Face beats, one leak |
| 6 | Explicit face close-up demanded during a fast exchange | Protecting user targets |
| 7 | Group scene: escort, defender, two attackers | Zoning, one clear exchange |
| 8 | A script paragraph in literary prose | Script-to-prompt translation |
| 9 | **Optics vocabulary:** one scene with three looks (35 mm handheld grain; 85 mm shallow tungsten; anamorphic halation) | Which terms the model responds to |
| 10 | **Length ladder:** the same scene at Compact, Standard, Extended; for clips over 10 s, test words per second (try about 15, 25, 35) | Where the model starts to drift or truncate |
| 11 | **Dialogue naturalness:** the same exchange as aphoristic lines vs spoken-register lines | Speech realism, mouth timing |
| 12 | **Face and body:** a seated two-person scene, Extended vs Compact | Plastic look, wooden actors |
| 13 | **Dialogue framing:** the same two lines in a medium-wide, a medium, and a close shot | Lip sync, face acting, listener beats |
| 14 | **Stealth takedown:** an assassin and a sleeping target, 15 s | Mode fit: one contact, silence, no flurry |
| 15 | **Last stand:** a wounded guard against a squad, 20 s | Overlap, fatigue, no clean resets, accumulating consequence |
| 16 | **Sparring:** master and student, 15 s | Legitimate pauses, light contact, play |
| 17 | **Street argument:** two people in a public lane, 15 s | Movement, overlap, onlookers, high arousal |
| 18 | **Farewell:** a platform or doorway, 15 s | Delay, silence 35–55%, hold after the departure |
| 19 | **Public vs private face:** the same bad news in a courtroom corridor vs a closed car | Display rules, mask strength |
| 20 | **Spatial navigation:** the same duel in an arena with three landmarks and a ledge, written with an arena card and ledger vs without | Lateral travel, bearing change, level change, anchor change |

## Rubric (score each clip 0 or 1 per line; sum)

**Action** (cases 1, 2, 3, 6, 7): contact is visible before the reaction; the reacting body's support and movement fit the force; the attack line meets the target at the crossing; with effects off in your head you can say who hit whom.

**Continuity** (case 3 and joins): position and facing match; held objects and injuries carry over; left/right and handedness did not swap.

**Look fit** (all cases): evaluate the declared medium and style. Realism needs plausible visible light and materials; animation needs its intended shape, edge and rendering language. Grain, pores, catchlights and imperfection are not universal requirements. Mark irrelevant items N/A.

**Wooden actors** (cases 4, 5, 12): responses follow cues; the listener is accounted for; movement or stillness serves the relationship; any prop use has purpose; no looped fidgeting. Neither moving both actors nor using props is required.

**Dialogue** (cases 4, 5, 11): lines sound like speech (breaks, fragments, repeats); delivery fits the line; mouth timing roughly matches; silence is used; the line length fits the clip.

**Mode and situation fit** (cases 14–19): pacing, pauses, and fail-state match the mode (a stealth clip is quiet and singular; a last stand has no clean resets); movement, distance, pace, and silence match the situation (a farewell is not seated); the mask matches the audience; the clip does not end on a still hold unless the profile calls for it.

**Spatial** (case 20 and fights): positions, paths or purposeful holds, facing, support and end states remain coherent; explicit travel or height targets are visible. Circling, level changes, landmarks and camera changes are assessed only when intended. Numeric diagnostics observe a design; watch continuous footage for execution.

**Prompt quality** (all): self-contained; no production scaffolding (the linter agrees); no claim the model cannot verify.

## Decision rule

Treat three clips per arm as a pilot, not a stable success rate. Necessary story and causality checks remain independently of model scores. For optional prompting techniques, compare repeated outcomes on relevant cases; inconclusive differences remain unproven. Record cases 9 and 10 in the model adapter.

## Results template

```
Date: ____   Model/version: ____   Clips per arm: ____
Case | Arm A score | Arm B score | Earliest failure (B) | Notes
```

## Reproduction and regression cases

Freeze task, outcome, exact dialogue, model/version, input mode, assets, runtime and settings. Record seeds when available and sampling uncertainty otherwise. Test one main change at a time. In case 9 vary one optical cue with other cues fixed; in case 10 retain required content across lengths. Case 12 compares whole packages and cannot isolate one face instruction. Save prompts, outputs, per-target scores and failures. No empirical results are bundled.

Behavioral regressions: fixed-camera doorway defense; two deliberately still speakers; locked dialogue containing negation; a short prompt retaining a required reveal; stylized imagery without pores/grain; first-frame input emphasizing motion. These check instruction behavior, not generated-video quality.

## Candidate release gate

Use v3.4.0 as this candidate's baseline unless the user chooses another. Run matched action, dialogue, static defense, style and continuation requests. Keep original inputs and actual outputs. Review target fidelity, action causality and invention, performance/listening, camera design, sensory specificity and continuity separately. A gain on one scene cannot erase a material regression on another. File count and prompt length are not creative scores.

Text-only forward tests assess writing behavior, not rendered quality. Run repeated video comparisons under matched model/version, references, duration and settings before claiming video improvement. If a material regression appears, repair or revert the affected route. This engineering beta has not completed video-quality acceptance; do not label it production-proven or guarantee quality for all future requests.

For beta maintenance, verify these behaviors independently: an explicitly flying character remains airborne under the supplied world rules; an impossible same-hand/same-time instruction yields concrete choices without silent replacement; an authorized fast fight retains evolving attacks and active camera design; a requested hard cut remains requested rather than becoming automatic continuous movement. Inspect actual delivered text, not keyword matches. Keep the full read log separately from any anonymous comparison. Run README's first-use commands from a fresh extraction, including a path with spaces, before distributing the package. Synthetic cut detection validates tooling only; it is not model-generation evidence.
