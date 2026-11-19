# Sound and Voice (Consolidated)

Combines overall sound design and character voice design. For conversational dialogue and delivery channels, see [spoken register](../dialogue/spoken-register.md).

## Overall sound design

This file handles the information and space conveyed by sound across the scene; [hit feel](../references/hit-feel.md) handles the instant of contact or force. These roles complement each other; do not stack a separate set of scoring rules onto every contact.

| Layer | Function | Candidates for a fight without dialogue |
|---|---|---|
| Environment | Place, scale, continuity | Rain on roof tiles, distant wind; preserve the same space across shots |
| Foley | Material and weight of movement | A foot taking weight, cloth settling, a brief ring of steel beginning at contact |
| Music | Relationship and rhythm | Lower it before contact and bring it back after the result; the main melody yields to important sounds |
| Silence | Highlight a decision or aftermath | Briefly reduce music and secondary sounds before a decision; retain spatial room tone according to intent |

Synchronization makes events readable. Counterpoint can place gentle music against tension, but cannot disrupt essential causality. Sound bridges use off-screen sound from the next scene; off-screen sound needs a direction and spatial basis. For music-driven work, mark the main beats and sections first, then decide which actions align. Theme variations change instrumentation, rhythm, or register; every scene need not receive a new track.

Sound does not merely explain the picture again: the image shows a stopped blade, while sound conveys metal still under pressure; dialogue does not narrate an obvious result. The prose may describe environment/contact sounds from existing sources and the selected quoted lines; actual execution channels and unverified capabilities follow [generation handoff](../references/generation-handoff.md). Mixing, detailed background music, dialogue-analysis cards, loudness, and exact lip-sync work belong in [audio post-production](../post/finishing-and-release.md). Judge the listening experience only after listening; waveforms or parameters alone do not establish that it sounds good.

### Subjective acoustics: reason from the character's current state

Use established contact or impact, physical capacity, attention, and narrative viewpoint to decide whether a subjective sound change is useful. This is not a fixed lookup of "hit → ringing ears" or "fear → heartbeat." A light touch, fatigue, and a heavy blow do not share the same sounds; an objective observing shot does not automatically enter the victim's hearing.

Where appropriate, choose a brief high-frequency ring, receding environment, prominent heartbeat, or temporary attenuation. Select only one that conveys information here, and provide an entry, a recovery, and continuity with the original spatial bed. Do not infer new deafness or brain injury from an effect, or present subjective treatment as a new physical injury. Strong ringing cannot appear without corresponding force.

Before extreme fear or a killing move, consider a "vacuum-like" subjective silence: reduce secondary music/environment and retain one small sound already present, such as a cuff rubbing or breathing. Silence follows the character's attention and established rhythm, not every attack; preserve sounds essential to reading key contact. This is subjective mixing, not an actual change to the medium or physical air.

Physiological sounds connect naturally to physical capacity and established exertion/impact timing; see [contact sound](../references/hit-feel.md#all-style-impact-context-reasoning). Detailed ringing filters, loudness curves, and precisely timed silence belong by default in [audio post-production](../post/finishing-and-release.md). Brief audiovisual intent may enter the prose; when capabilities are unknown, mark them unverified outside it and retain the post-production plan. Complex mixing instructions stay in post; do not force a platform change. Adapt to the user's goal when they request purely visual input. Pure final prompts contain no module explanations; a sound plan or waveform is not evidence of a successful listening check.

## Character voice design

When the scene contains a human voice, select the applicable voice texture and rhythm by default. A compact version may simplify these; no additional module authorization is required. This file handles character voice properties, not the four environment/foley/music/silence layers of [scene sound design](sound-and-voice.md), or the mixing and loudness of [audio post-production](../post/finishing-and-release.md).

### Six parameters (design as needed; not all are mandatory)

| Parameter | Design question | Candidate audible descriptions |
|---|---|---|
| Pitch and timbre | How do relative pitch, perceived resonance, and texture distinguish characters? | Chest/head resonance, low/clear/raspy/rounded; choose compatible descriptions rather than stacked synonyms |
| Breath | What are the support, breathing rhythm, and breath points? | Air escaping at sentence ends, shallow or held breath under stress, breath placement within a long line |
| Articulation and pace | How tight is articulation, and what are the speed, pause, and stress habits? | Clear or connected onsets, swallowed sounds at speed, pauses mid-line or at the end, stress on verbs |
| Accent and social background | How do established region, occupation, and era influence the voice? | Setting-based pronunciation and particles; a generic "period voice" does not replace concrete design, and accent does not prove social rank |
| Pattern of emotional change | How does this character's voice change with emotion? | Raised or lowered pitch, broken or steady breath, tight or loose articulation, whether pace or breath changes first; not one formula for everyone |
| Relationship mapping | How does the voice adapt to different listeners? | Differences in pitch/pace/breath, who follows whom, and around whom someone changes their delivery; more than a strong/weak classification |

### Boundaries

- Voice parameters support dubbing and TTS. In video prose, attach a brief voice-texture/rhythm cue to the quoted line (see [spoken register](../dialogue/spoken-register.md)); do not include the parameter table.
- Quoted lines and brief voice cues are inline by default. Actually controllable tool parameters and execution channels follow [generation handoff](../references/generation-handoff.md); flag anything unverified and keep complex parameters in production notes. Verify sound effects, dialogue, timbre control, and exact lip sync separately.
- Never write "voice approved" without listening. Parameters not actually generated are candidates, not guarantees. Do not automatically upload, pay, or call tools.
- Low does not mean strong, and clear does not mean weak. Do not invent a past, region, or social class to fill parameters; use established facts or provisional design authorized for this task.

### Handoffs

- [Dialogue design](../references/dialogue-engine.md) handles text and intent; this file does not repeat its four-layer model.
- [Scene sound](sound-and-voice.md) handles environment/foley/music/silence. Timbre is a character property, not a new sound layer.
- [Mixing and loudness](../post/finishing-and-release.md) handles post-production; voice design does not mean mixing is complete.
- Record the six parameters in the [character continuity card](../references/character-and-performance.md#handoff-ready-character-consistency-card), carrying versions and approval status across segments. Record changes caused by the current state separately rather than changing the voice every segment.

## Sound strategy routed by context

The Context Profile determines sound density and silence, rather than filling every scene uniformly:

- **Stealth/assassination:** near silence, one controlled sound (gravel under a boot, one breath); silence carries tension.
- **Cornered struggle:** broken breathing, clothing, continuous impacts, no quiet recovery.
- **Sparring:** light wooden or padded contact, casual speech, laughter.
- **Ritual duel:** near silence, one ritual sound; sound breaks when the code breaks.
- **Street argument:** crowd, shouting, overlapping voices, multiple layers.
- **Farewell:** let environmental tails linger and retain the space's sound after someone leaves (a platform, wind outside).
- **Whisper/secret:** breathing leads, with environmental noises suggesting threat.
- **Post-exertion:** breathing, metal landing, clothing rubbing, lines broken by breath.

Choose one leading sound and let the others yield. Native-audio availability still requires an actual test.
