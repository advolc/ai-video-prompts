# Model evidence and capability index

## Evidence classes

**Design discipline:** methods for the writing agent (causality, intention, spatial reasoning). No claim that the video model understands the analysis terminology.

**Rendering hypothesis:** expected responses to words such as FACS units, Laban effort, Rembrandt lighting or anamorphic halation. Use the concept internally if useful; describe the visible behavior/result. Direct terminology may be retained where useful or tested, but is not a deterministic control.

**Documented interface:** a dated source describes an available input, control or workflow on a named endpoint. This does not certify adherence or artistic quality.

**Observed generation:** an actual output, with input/settings/version and sample count, supports a bounded observation. No auditable original model-generation sample is bundled. Follow the [observation record](../references/source-scope.md#model-observation-record); unspecified historical clips are not empirical support. Do not convert a documented feature into a measured success rate.

## Dated capability matrix

Checked 2026-11-14. Read source before execution because endpoints and versions change. This is a small maintained starting set, not a market-wide ranking. Unknown entries remain unknown; no platform is assumed incapable from missing evidence.

| Model and surface | Documented input/workflow | Audio and speech | Length / execution caveat | Skill-owned render evidence |
|---|---|---|---|---|
| Sora 2, OpenAI video workflow | Image `input_reference` anchors the first frame; prose describes ensuing motion | Official guide describes dialogue/audio prompting, with a separate speaker-labeled dialogue block | Guide and SDK documentation may differ by revision; recheck endpoint limits rather than hard-code a universal duration | None; contact, micro-acting and density untested |
| Gemini Omni 1.2 Flash, Gemini API | Text/image/video input; up to six reference images; conversational editing/extension | Native audio documented; exact line fidelity requires tests | Up to 15 seconds documented; account/endpoint availability must be checked | None; quality and timing untested |
| Veo 3.1 preview IDs, Gemini API | Legacy preview route | Do not infer current execution from old feature descriptions | Official page says these preview IDs shut down 2026-10-22; other hosting surfaces need separate verification | None |
| Other versions, hosted tools and models | Verify actual interface using [adapter checklist](README.md) | Separate effects, speech and lip sync | Unknown until checked | None bundled |

Sources: [OpenAI Sora 2 prompting guide](https://developers.openai.com/cookbook/examples/sora/sora2_prompting_guide), [Google video routing/deprecation](https://aistudio.google.com/docs/video), [Gemini Omni documentation](https://aistudio.google.com/docs/omni). These source-backed facts do not claim observed performance. For Sora's documented dialogue layout, `--format platform` permits the labeled block while preserving exact lines and their associated visible delivery; inline speech remains the platform-neutral default.

## Maintaining an entry

Copy [adapter template](_adapter-template.md) for a tested endpoint/version. Record official sources separately from empirical inputs, settings, outputs and failures. Update this index and supersede dated observations when versions change. Mark rendering terminology as untested once here and in the selected adapter rather than repeating a warning in every sentence. Retain local caveats only when they change a specific decision.
