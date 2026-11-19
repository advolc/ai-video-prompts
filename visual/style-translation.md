# Translating Reference Style


Begin with [reference classification](../ux/interaction.md), analyzing only the dimensions the user wants to inherit. This is basic scope classification, not optional depth; even compact paths use it to prevent incorrect inheritance. Keep these two groups of analytical dimensions separate.

## Seven visual-art dimensions and three audiovisual dimensions

**Seven visual-art dimensions** ("borrow the visual style" defaults only to the needed items here):
1. Form and proportion: head/body ratios, shape simplification, realism/exaggeration; deformation in moving references belongs to this dimension over time.
2. Line and edge: presence of outlines, weight, line quality, soft/hard edges; do not merge outlines into form/proportion.
3. Color: relationships, saturation, value hierarchy, temperature.
4. Light and shadow: source logic, contrast, shadow and highlight treatment.
5. Material and texture: material rendering, texture density, brushwork/grain, render finish.
6. Space and perspective: perspective, depth of field, depth layers, negative space, background density; record static composition here.
7. Effects rendering: realistic particles, graphic color blocks, ink strokes, or linework; borrow representation, not abilities, power, or new objects.

**Three audiovisual dimensions** (inherit only when explicitly requested):
8. Camera movement: changes in viewing position and the feel of shot duration.
9. Editing: cutting rhythm and transitions.
10. Sound: effects texture, music style, silence.

Borrowing visual style does not automatically inherit camera movement, editing, or sound. Extend to the relevant audiovisual dimensions only for an explicit request for "this camera movement/editing rhythm/sound feel." Stills support observable static items only; deformation needs before/after video evidence, and sound requires actual listening. Classification still follows the reference inputs; this table only refines what is borrowed. Seven art dimensions do not mean all seven must be borrowed. If the user wants only color and material, take only those two and retain established settings elsewhere. Handle gaps through permitted assumptions rather than expanding reference authorization.

**Separate the reference's content:** "borrow visual style" primarily means rendering, light/shadow, color, and materials. Unless explicitly requested, never import its specific location, weather, costume, weapon abilities, or "counterattack after severe injury" plot structure into the new film.

## Procedure

Inspect accessible material → extract 3–5 candidate signatures → describe visible relationships by dimension → translate into plain prose → pilot → revise.

Each visual signature must be assigned to one of the seven dimensions and labeled. One item serves one dimension; split combinations spanning dimensions. The hue of dark-red leaves is color; a narrow-shouldered, elongated silhouette is form/proportion; straight rows of trees receding are space/perspective; cold side light catching an existing blade is light/shadow. If "gray-black figures separating from red ground" involves both hue and form, split it into color separation and shape simplification; do not force color differences into form. Index tags such as "red/gray, geometry, material" are not fully defined signatures.

Record explicitly authorized audiovisual inheritance separately under the corresponding three dimensions, not within visual-art signatures. Do not force 3–5 candidates: if the user borrows two dimensions, record only supported items. Test a signature counterfactually: does removing this element remove the distinction the user wants? Mark strong inheritance only after user confirmation; a director's name cannot override the user's work.

## Relating signatures to theme (optional depth)

Enabled by default; it may be omitted for an explicit "compact/lite" request. For each candidate, ask which dimension it belongs to and what thematic expression might be lost without it. This table illustrates possibilities, not fixed genre recipes or inevitable psychological effects. Adapt only where current elements and themes support them.

| Signature | Dimension | Theme it may serve | Candidate difference if removed |
|---|---|---|---|
| Dark-red hue and low value of existing leaves | Color | Cost and estrangement in the martial world | May weaken this film's established association of cost with color; does not require new red leaves |
| Narrow shoulders, elongated body, inward-contained silhouette | Form and proportion | Restraint under pressure | A looser form may weaken this film's established self-control |
| Gray-black/dark-red separation of existing figures and ground | Color | A person surrounded by the environment yet still readable | Figure/ground separation may weaken; do not merge with the previous item into a cross-dimension signature |
| Straight tree rows receding into light mist | Space and perspective | Order and uncertain exits | May weaken directional pressure in depth; trees and mist both require an established basis |
| Cold side light catching only an existing blade edge | Light and shadow | A decisive action briefly revealed | May weaken a narrative highlight accent; does not authorize a new weapon |

After user confirmation, record the single dimension, signature, and thematic relationship in the [style card](style-library.md), carrying both signature and relationship across segments. Do not force a theme onto every signature. An unrelated element may remain decorative rather than strong inheritance. Candidates do not replace reasoning for this scene or authorize copying example objects into a new project.

Card fields: `Style ID | Signature elements | Variable elements | Excluded elements | Prompt fragment | Validation status`. Exclusions list only the likeliest current mistakes; convert final prose to positive depiction rather than pasting the entire card into a model. Separate candidates from observations: unseen material is not observed; an ungenerated pilot is not verified. For variants, list retained signatures first, then change one dimension and compare within the same scene for continued recognizability.

## Restraint in style mixing (optional depth)

Enabled by default; it may be omitted for an explicit "compact/lite" request. Choose the main style, then one secondary element. The main style supplies over 70% of visual language as a design intention, not a claim about measurable pixels or components. The secondary element enters only one of the seven visual-art dimensions, such as light or material, rather than averaging two cards across dimensions. When color, light, material, and form from different works feel fragmented, reduce secondary elements before adding more style terms. Do not use this section for a single-style request.

| Feeling | Three candidate combinations for the user, not fixed answers |
|---|---|
| Isolation | Cool-gray distant view + negative space + locked camera; small warm-lit room + doorway separation + slow retreat; daylight wasteland + low saturation + long shadows |
| Oppression | Narrow frame + top light + slow push; low-angle giant mass + mist + low frequencies; high-contrast side light + nearby occlusion + silence |
| Freedom | Open horizon + lateral follow + clear wind direction; bright grassland + deep focus + sustained action; rooftop height changes + warm light + outward negative space |
| Mystery | Partial light + occlusion + off-screen sound; reflections in mist + shallow focus + one focus pull; black-and-white negative space + distant figure + delayed footsteps |
| Warmth | Soft side light + analogous warm hues + shared frame; practical tabletop lamp + old wood grain + slow approach; overcast window light + low contrast + everyday foley |
| Desolation | Earth-gray distant view + repeated ruins + wind; cold-white salt flat + high horizon + tiny lone figure; rust-orange wreckage + locked camera + mechanical decay |

When the user says only "I want isolation/oppression/freedom," offer the corresponding 3 combinations or accept their own. Do not choose the first for them or paste this table into prompts as a default answer.

Select only one relevant card from the [style library](style-library.md) as needed. Without references, these are creative proposals. [Color](composition-and-color.md), [composition](composition-and-color.md), and [light](../lens/physical-light.md) provide detail; stage the reading when the budget is limited rather than loading everything.

