# Dialogue Design Card Template

Usage and shared fields: [record selection](../../core/records.md). Reference one scene/version record; do not re-enter unchanged facts.
An optional expanded record for [dialogue design](../../references/dialogue-engine.md), kept in design/production notes. It is not model input, a script-parsed format or a form the user must fill completely. Relevant design checks run by context without a separate module-unlock step.

```yaml
meta:
  id: "______"
  scene: "______"
  genre_and_style: "______"
  facts_status: "Separate locked facts from candidate assumptions: ______"
  delivery_route: "Inline design plus verified native execution or post voice: ______"
characters:
  speaker:
    name: "______"
    language_dna:
      sentence_length: "______"
      vocabulary: "______"
      address_and_tic: "Address terms, habitual phrasing and frequency: ______"
      under_pressure: "______"
  listener: "______"
relationship:
  current_power: "______"
  known_information_boundary: "______"
  intended_change: "______"
dialogue:
  intention: "Who is asked to do what: ______"
  subtext: "Unspoken need/information, where applicable: ______"
  speech_action: "Transitive action verb: ______"
  style: "Genre + language DNA + body load: ______"
  main_technique: "A relevant depth technique or deliberately direct speech: ______"
  candidates: ["______", "______"]
  selected_text: "______"
performance:
  visible_action: "Compatible body signals, ordered by beat: ______"
  voice_and_breath: "Voice direction: ______"
  emphasis_and_pause: "Complex annotations stay in production notes: ______"
  in_frame_or_voiceover: "______"
constraints:
  frozen_facts: ["______"]
  motion_and_speech_window: "Action window and conflicts: ______"
  readthrough_status: "Pending or actual read-through result: ______"
  lip_sync_status: "Actual capability/use and pending verification: ______"
  continuity: "Carry syllables, relationship and injury state: ______"
```

## Filling logic (not an export pipeline)

```text
Freeze plot facts, information boundaries and action outcomes.
Check intention / subtext / speech_action / style where relevant.
If a gap changes locked facts, ask only the essential question and continue independent work.
Otherwise mark a candidate as a candidate, rather than an established fact.
Write a few alternatives -> check language DNA and technique -> select one.
If speech conflicts with breath or action, shorten it or propose an action window/voice-over.
If not actually read aloud, keep readthrough_status pending.
Detailed analysis card -> production notes / post voice.
Selected quoted speech + speaker + brief delivery -> prompt timeline by default.
Verified native support determines execution; unknown speech/sync is labeled outside prose.
Visible performance -> actual event/load check -> Lens translation and lint -> self-contained prompt.
```

Filling this card does not run voice/sync tools or certify a read-through. Deliver copyable prose by default; show engineering records only when requested. Card analysis and YAML stay outside platform input.
