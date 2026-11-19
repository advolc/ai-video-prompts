# Performance and Facial-Detail Design Card

Usage and shared fields: [record selection](../../core/records.md). Reference one scene/version record; do not re-enter unchanged facts.
An optional record for the relevant checks in [performance design](../../references/performance-and-psychology.md). It does not change the main prompt or export format. Fill it from the established story rather than asking the user to invent a psychological profile from scratch.

## Character state

```yaml
character: "Character and scene version: ______"
current_objective: "What is wanted from whom now: ______"
obstacle: "Existing obstacle: ______"
action_verb: "Plead with whom / conceal what / intimidate whom: ______"
hidden_fear: "Supported concern or explicit candidate: ______"
physical_tell: "A visible signal compatible with the action: ______"
```

## Performance fields

| Field | Content | Check |
|---|---|---|
| Gaze path | Origin ______ -> target ______ -> event-relative timing ______ | Real target, visible from the shot; no arbitrary millisecond precision |
| Facial detail | Lids ______; jaw ______; breath ______ | Candidates may remain empty; select only useful details |
| Physical quality | Weight ______; rhythm ______; relation to counterpart/exit ______ | Compatible with support, grip and held weapons |
| Alternatives and routing | Body alternative ______; optional reaction shot/post plan ______ | Protected targets require the user's accepted alternative; complex analysis stays in notes |
| Verification | Observed result ______; still pending ______ | No video means no claim that acting passed |

## Candidate wording

```text
Action-response candidate: When ______ (established cue), ______ (person) first ______ (visible attention/body choice), then ______ (goal-driven action), ending at ______ (visible state).
Camera candidate: ______ (size/angle) accommodates ______ (required gaze target or body part).
Texture candidate: ______ (non-decisive physical detail that can be reduced).
Production note: ______ (intent, complex pause, post alternative, pending check).
```

Automatic text drafting means deriving candidates from these fields, not executing a script or authorizing new action. Retain candidates that fit the unit: action in the design timeline, framing in camera tasks, and reducible detail in performance/texture. Do not hide a distinct action inside camera wording to evade capacity checks. Replace vague wording first; propose a separate reaction shot only when needed.

Before model input, merge selected candidates into self-contained prose with the look and character identity; remove card names, unit IDs, engineering labels and time ranges. Rewrite exclusions as visible conditions. Large action favors body signals, while fine facial work needs a low-motion window. Control and management details remain outside prose.
