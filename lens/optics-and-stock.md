# Pass 1: Optics and Stock

Evidence: this is a design vocabulary; direct renderer response follows [evidence classes](../models/capabilities.md#evidence-classes). Preserve the craft even when the final prompt uses ordinary visible language.
Purpose: give the image a physical camera behind it, which counters the clean, weightless AI look. Every term is **"confirm per model"**: models differ in how much they respond to each, so test (`evals/cases.md`, case 9) and record results in `models/`.

Use terms in the Look anchor and in camera sentences. Pair each term with what it looks like when the shot size can show it.

## 1. Focal length and perspective

| Focal feel | Look | Use |
| --- | --- | --- |
| 14–24 mm | Stretch, depth, edge distortion, environment dominates | Architecture, chase, disorientation; avoid on close faces |
| 28–35 mm | Natural wide, shoulder-to-shoulder presence, slight room feel | Handheld drama, two-shots, walking scenes. 35 mm is the classic "cinema" default |
| 50 mm | Neutral, close to a human view | Anything when you want no lens opinion |
| 85 mm | Compressed face, flattering, clean separation from background | Portraits, intimate dialogue, tense close-ups |
| 100–135 mm | Stronger compression, isolated subject, background rises | Isolation, longing, surveillance feel |
| 200 mm+ | Heavy compression, flattened layers, voyeuristic | Observed from far, crowds as texture |
| Macro / probe | Extreme detail of eye, hand, object | Contact close-ups, ritual detail |

## 2. Aperture and depth of field

| Term | Look |
| --- | --- |
| Wide open (T1.4–2.8), shallow depth of field | Background melts to soft shapes, one plane sharp |
| Mid (T4–5.6) | Subject sharp with readable surroundings |
| Stopped down (T8+), deep focus | Foreground to background sharp; threat in layers |

Write the focus plane as a depiction: "the cup's rim stays sharp while Wu's face softens behind it." A rack focus needs new information to hand off to (a reveal, a reaction); avoid it mid-fast-action.

## 3. Lens character

| Character | Look |
| --- | --- |
| Spherical, modern, clinical | Clean, high micro-contrast |
| Vintage or softer glass | Lower contrast, soft highlights, gentle halation |
| Anamorphic | Oval bokeh, horizontal streak flares, mild edge softness, wide frame (about 2.39:1) |
| Diffusion filter (Pro-Mist style) | A faint glow around practical lights, softened highlights; also softens skin micro-detail |
| Vignette | Corners darker, subject drawn inward |
| Chromatic fringing | Faint color edges at high-contrast borders, mostly at frame edges |
| Lens breathing | The image slightly changes scale as focus shifts |
| Practical flare | Streak or veil from a visible lamp, window, or flame |

## 4. Stock, sensor, grain

| Look | Character |
| --- | --- |
| 35 mm film, tungsten-balanced stock (Kodak Vision3 500T style) | Warm practicals, visible grain in shadows, rich blacks |
| 35 mm film, daylight stock (250D style) | Cleaner daylight, finer grain, natural color |
| Eterna-style film | Cooler greens, soft contrast, gentle skin |
| 16 mm | Coarse grain, softer detail, documentary or period texture |
| 65 mm large format | Very fine grain, huge detail and depth |
| Digital cinema sensor | Clean, wide dynamic range, grade carries the look |
| Fine, medium, coarse grain | Grain lives in shadows and midtones, moves frame to frame; write it as film grain, never "noise" |
| Halation | A red-orange glow bleeding around bright highlights on film, best around lamps and neon |
| Highlight roll-off | Soft shoulders, no hard clipping |

Brand names are shorthand: always pair with the effect ("warm practicals, grain in the shadows") so a model that does not know the brand still gets the look.

## 5. Grade and color

| Term | Look |
| --- | --- |
| Teal and amber | Cool backgrounds, warm skin |
| Bleach-bypass style | Silvery, desaturated, high contrast, gritty |
| Low saturation, skin tones preserved | Restrained palette, faces still read |
| Warm tungsten palette | Amber highlights, deep warm shadows |
| Cool overcast palette | Blue-grey, flat soft contrast |
| Lifted blacks | Faded, filmic shadows |
| Crushed blacks | Dense, dramatic shadow |

Grade is not new content. It does not add objects or change locked facts.

## 6. Shutter, frame rate, motion rendering

| Term | Look | Use |
| --- | --- | --- |
| Natural motion blur (180° shutter feel) | Smooth, filmic motion | Default |
| Crisp, staccato motion (narrow shutter feel) | Little blur, choppy sharp movement | Combat, impact |
| Dreamy trailing blur | Smeared motion | Memory, drift |
| 24 fps cadence | Filmic | Default |
| High-speed slow motion | Droplets, cloth, dust hang | Only on request, one beat |

## 7. Camera behavior

| Behavior | Feel |
| --- | --- |
| Locked-off tripod | Stillness, observation, weight |
| Dolly in or out | Smooth approach or withdrawal, pressure or release |
| Slow push-in | Gradual intimacy or threat |
| Steadicam float | Smooth following glide |
| Handheld with operator's breath | Small organic drift that settles when the subject stops |
| Whip pan | Sudden redirect; landing must be identifiable |
| Crane or high rise | Reveal of layout and scale |
| Orbit | Control, assessment; keep axis readable |

Motivate every move: write what causes it ("the camera drifts left as he stands", "the push-in starts when Wu stops speaking").

## 8. Look presets (examples of context-to-look mappings; see section 10 to route)

| Scene | Look anchor |
|---|---|
| Intimate power dialogue | 85 mm, shallow depth of field, warm tungsten key, low-key shadows, fine grain, locked-off with a slow push-in |
| Gritty realistic combat | 35 mm handheld with operator's breath, narrow-shutter crisp motion, bleach-bypass desaturation, medium grain |
| Period wuxia, lantern night | Anamorphic feel, soft halation around flames, deep shadows, warm amber against cool blue moonlight, medium grain |
| Quiet interior melancholy | 50 mm, window light, low saturation with skin preserved, lifted blacks, fine grain, locked-off |
| Neon city noir | 35 mm, wet streets, halation around signs, teal and amber, fine grain, steady dolly |
| Stylized 2D or 3D animation | State the animation medium first; use virtual-lens terms sparingly (depth of field, bloom, subtle film grain overlay); skip stock names |

## 9. Contradictions to avoid

- Anamorphic and spherical in one look; fisheye and compression telephoto; shallow depth of field and "everything sharp, deep focus".
- Heavy diffusion filter while asking for visible pores.
- Narrow-shutter crispness with dreamy trailing blur.
- Handheld operator's breath and locked-off tripod in the same shot (a cut between them is fine).
- Day-bright grade with a night setting.
- More than three stock or grade terms; pick the dominant one.

## 10. Routing the look from context

Choose the look from the Context Profile (`core/context-routing.md`). These are creative starting points; actual rendering behavior uses the evidence record.

| Context | Lens and camera leaning | Light and grade leaning |
|---|---|---|
| Intimate talk, confession | 85–100 mm, shallow depth of field, locked or a very slow push | Single warm practical, deep shadow, fine grain |
| Panic, ambush, chaos | 24–35 mm handheld, narrow shutter, camera as participant | High contrast, coarse grain, harsh or mixed light |
| Stealth | Long lens from distance, a slow creep or locked, one close detail at the contact | One hard source, deep shadow, cool and low saturation |
| Ritual, formal | Wide, symmetrical, locked, slow push; anamorphic or clean spherical | Even stable light, restrained palette |
| Public argument | 28–35 mm handheld, deep focus for crowd layers | Ambient daylight or street light, natural contrast |
| Farewell | 85–135 mm compression, lingering locked frame; a hold after the departure | Soft backlight, low contrast, lifted blacks |
| Dominance and menace | A lower angle, steady, modest lens; the dominant given room and the other cropped | Directional light with a clean edge on the dominant |
| Grief | 50–85 mm, steady, patient | Soft window light, low saturation |
| Comic | Wider, brighter, stable framing | High key, saturated, clear |
| Horror | Slow push, off-center framing, space left empty | Shadows, a motivated source that does not reveal everything |

If the scene changes profile mid-clip, the look may shift at the turn; write it as a depicted change (the light narrows, the lens pushes in), not as a second look anchor.
