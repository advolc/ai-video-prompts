# Evals: find out what actually works

v3 has not been benchmarked. These cases are how you find out. Your own test of v1 against v2 was the first evidence either design had; this harness makes that repeatable.

## Protocol

For each case, run **Arm A** (your current best prompt, or the v1 output) and **Arm B** (the v3 Extended output). Generate at least 3 clips per arm on your target model. Score blind if you can (someone else shuffles the clips). Record results in `evals/results.md` using the template below.

## Cases

| # | Case | Stresses |
|---|---|---|
| 1 | One-on-one sword duel, one exchange (parry then counter) | Contact, support, consequence |
| 2 | Long weapon vs short weapon, close-in | Weapon logic, distance |
| 3 | Same fight, second clip, after a stagger and a dropped weapon | Seams and state carry-over |
| 4 | Two characters, a soft threat across a table, no fight | Status, listening, prop business |
| 5 | A character hides a wound while talking | Face beats, one leak |
| 6 | Explicit face close-up demanded during a fast exchange | Protecting user targets |
| 7 | Group scene: escort, defender, two attackers | Zoning, one clear exchange |
| 8 | A script paragraph in literary prose | Script-to-prompt translation |
| 9 | **Optics vocabulary:** one scene with three looks (35 mm handheld grain; 85 mm shallow tungsten; anamorphic halation) | Which terms the model responds to |
| 10 | **Length ladder:** the same scene at Compact, Standard, Extended | Where the model starts to drift or truncate |
| 11 | **Dialogue naturalness:** the same exchange as aphoristic lines vs spoken-register lines | Speech realism, mouth timing |
| 12 | **Face and body:** a seated two-person scene, Extended vs Compact | Plastic look, wooden actors |

## Rubric (score each clip 0 or 1 per line; sum)

**Action** (cases 1, 2, 3, 6, 7): contact is visible before the reaction; the reacting body's support and movement fit the force; the attack line meets the target at the crossing; with effects off in your head you can say who hit whom.

**Continuity** (case 3 and joins): position and facing match; held objects and injuries carry over; left/right and handedness did not swap.

**Plastic look** (all cases): skin shows believable variation (not uniform); lighting has a visible source and direction; eyes have catchlights; hair and cloth show imperfection; the image has a physical camera quality (grain, depth, lens character).

**Wooden actors** (cases 4, 5, 12): both people move during the clip; the listener reacts; a prop is handled with purpose; posture reads status without a line; no looped fidgeting.

**Dialogue** (cases 4, 5, 11): lines sound like speech (breaks, fragments, repeats); delivery fits the line; mouth timing roughly matches; silence is used; the line length fits the clip.

**Prompt quality** (all): self-contained; no production scaffolding (the linter agrees); no claim the model cannot verify.

## Decision rule

Keep a rule or pass only if arm B beats arm A on that rule's rubric lines across at least 3 clips on at least 2 cases. If it shows no difference, cut it or mark it "unproven". Cases 9 and 10 write directly into the model adapter (`models/`).

## Results template

```
Date: ____   Model/version: ____   Clips per arm: ____
Case | Arm A score | Arm B score | Earliest failure (B) | Notes
```
