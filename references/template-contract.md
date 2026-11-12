# Design Ledger Contract

v1 used FIXED / EVENT / SEAM blocks as the authoring surface and a script to export them. v3 writes the **prompt first** and treats ledgers as an optional internal check. The export script is retired; `scripts/lint_prompt.py` replaces it.

## 1. When to use a ledger

Only when the user asks for the engineering view, or when planning a long multi-clip sequence. Never in the copy block.

## 2. Ledger fields

**Project card:** `genre/format | length | world rules | aspect/resolution | model and verified conditions | reference inputs actually used | locked facts`

**Character card:** `ID/version | face structure and asymmetry | skin and hair | costume materials and wear | handedness | weapon or prop | voice (pace, register, DNA) | status default | locked looks`

**Scene card:** `ID/version | layout and anchors | light sources (direction, color temperature) | atmosphere | props and their states | camera paths`

**Clip card:** `clip ID | duration | Tier A events | beats (Tier B) | texture choices (Tier C) | speech and delivery | start state | end state | camera tasks | test conditions`

**Seam card:** `position and facing | support and posture | held objects | injury and stamina | ability state | environment state | light | prop state | distance`

## 3. Rules

- A ledger is derived from the prompt and the design record. It does not constrain the prompt's richness.
- Texture (Tier C) and performance (Tier B) never sit in an event-count budget. Only Tier A is counted.
- Fields marked "verified" need a source (docs, the user, or a clip). Everything else is "assumed" or "untested".
- Keep ledgers outside the copy block and unlinked to model syntax.
