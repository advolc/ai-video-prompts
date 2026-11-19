# Pass 3: Skin, Hair, and Material

Evidence: this is a design vocabulary; direct renderer response follows [evidence classes](../models/capabilities.md#evidence-classes). Preserve the craft even when the final prompt uses ordinary visible language.
The plastic AI look comes from uniform skin, perfect symmetry, smooth hair, clean cloth, and flawless surfaces. The cure is **specific, asymmetric, imperfect detail that the shot size can show**. 

## 1. Principles

1. **Specific beats pretty.** Replace "beautiful, flawless, glowing" with structure and texture. The words "perfect", "flawless", and "airbrushed" tend to pull toward the smooth look (a hypothesis to test).
2. **Asymmetry.** Faces and bodies are not mirror images. Give each new character **one** subtle asymmetric identifier: a brow set slightly higher on one side, a nose with a faint bend, a lid that droops a little. One, not a stack of scar plus aging plus crooked nose.
3. **Life load.** Texture comes from what the person does: sun on a laborer's cheeks, thick knuckles, a clerk's ink-stained fingertip, a swordsman's callused palm edge.
4. **Match the shot size.** Detail that cannot be seen is wasted words (section 6).
5. **Locked designs win.** A user's reference image, established face, or approved costume is never altered. Add only compatible texture. Never add scars, age, or damage that change identity.
6. **Stylized media** (clean 2D, idealized 3D) do not get imposed pores or aging. Use the outline, shading, and texture the style allows.

## 2. Face and skin lexicon

| Feature | Depict as |
| --- | --- |
| Pores | Visible fine pores across the nose and cheeks |
| Fine lines | Crow's feet at the eye corners, forehead creases, lines running from nose to mouth corners |
| Under-eye | Slight darkness, a faint blue vein, a soft tear-trough shadow |
| Vellus hair | Fine pale hair catching light along the cheek and jaw |
| Sebum sheen | A faint shine on the nose bridge, forehead, and chin; matte cheeks |
| Subsurface glow | Ears and nostril edges glow warm red when backlit; fingertips pink against a lamp |
| Flush | Cheeks and nose tip reddened by cold; blotches creeping up the neck under stress |
| Freckles, sun spots, moles | A few, unevenly placed |
| Scar or mark | Thin pale line through one brow; fine and old unless locked otherwise |
| Stubble | Uneven, denser at the jaw, thinner at the cheek, grey flecks |
| Lips | Vertical lines, dry patches, a split at one corner, a film of moisture |
| Eyes | Slightly red lid rims, a moist line along the lower lid, uneven lash direction, a faint tint in the whites |
| Teeth | Slightly uneven, a faint yellow near the edges, one a little crooked |
| Brows | Hair growing in different directions, a stray hair |
| Neck, throat | Tendons, a pulse showing at the throat, a swallow |
| Hands | Knuckle creases, raised veins, ridged nails, a callus, dirt in the cuticle, a faint scar |
| Sweat | Beads at the hairline and temple, a bead running down the jaw, shine on the collarbone |
| Tears | A wet rim along the lower lid, a bead gathering, a track of shine |
| Goosebumps | Raised skin on the forearm in cold or fear |
| Bruise, injury | Color matches the age of the injury; swelling and stiffness change movement |

## 3. Hair

| Feature | Depict as |
|---|---|
| Flyaways | A few strands lifting off the crown, catching rim light |
| Oil or matte | A sheen along the parting; dry ends |
| Wet | Clumped into dark strands, a drop at the tip |
| Grey pattern | Silver at the temples, a streak through the fringe |
| Beard | Thicker at the chin, patchy at the cheek |
| Cloth contact | A strand caught in the collar |
| Style under stress | A topknot loosening, a tie slipping |

## 4. Fabric and material

| Material | Depict as |
| --- | --- |
| Linen, hemp | Visible weave, soft creases, a rough nap at the cuff |
| Wool | Fuzzy surface, pilling at the elbow |
| Silk | Liquid sheen that shifts with the fold |
| Cotton padded jacket | Quilted ridges, flattened at the elbow |
| Leather | Cracks at flex points, polish where hands touch, a dull patina |
| Metal | Micro-scratches along the edge, a thin oil film, temper color near the guard |
| Wood | Grain, a polished patch where a hand rests |
| Porcelain / glazed ceramic | A hairline craze in the glaze, a chip on the rim |
| Paper | Fibres, a curl at the corner, a damp mark |
| Rope | Frayed fibres, darkened where gripped |

**Wear comes from use.** Polish where hands touch; patches or strain where cloth bends; creases at elbows, knees, and the lap from sitting; a collar darkened by sweat; mud at the hem. New, formal, or gifted items stay clean. Wealth does not equal quality and poverty does not equal rags. Do not wear a weapon into failure: wear must not break a function the story needs.

**Wet cloth** darkens and clings; **dry cloth** drapes. Match the weather.

## 5. Anti-plastic checklist

- Skin varies by region: shine here, matte there, redness at the nose, pale at the temple.
- Hair and cloth are imperfect (flyaways, creases).
- Surfaces hold history: dust, scratches, polish, stains.
- Nothing is evenly lit and evenly colored.
- One asymmetric identifier per new character; none added to locked ones.
- No "perfect, flawless, airbrushed, ultra-detailed" language.
- Do not pair heavy diffusion with pore detail (the optics pass would blur it).

## 6. What each shot size can show

| Shot | Show | Skip |
|---|---|---|
| Wide | Silhouette, hair outline, cloth drape, sheen on wet surfaces | Pores, lashes, lip texture |
| Medium | Face shape, major lines, hair, collar, hands | Fine vellus, pores |
| Medium close-up | Eyes, brows, stubble, lips, lines, fabric weave | Iris detail |
| Close-up | Pores, vellus, lip cracks, eye moisture, nail ridges | Whole-body detail |
| Extreme close-up | Iris structure, lash roots, skin grain, a single bead of sweat | Everything else |

## 7. Examples

- *Medium close-up, English:* "Chen is in his mid-fifties, heavy-lidded, with grey stubble that thins along the cheekbones; deep lines run from his nose to the corners of his mouth, and the skin under his eyes is slightly dark, with one faint blue vein. His left brow sits a little higher than his right. A thin shine rests on his nose bridge and forehead while his cheeks stay matte."
- *Hands:* "His knuckles are thick, the nails ridged, a callus on the inside of the right thumb; the cuffs of his coat are rubbed pale where his forearms rest on the chair."
- *Alternate wording:* "He is in his early fifties, with heavy lids and grey stubble thinning over the cheekbones. Deep folds run from the nostrils to the mouth corners; a faint blue vein shows beneath slightly darkened eyes. His left brow sits a little higher. A thin sheen catches the bridge of his nose and forehead, while his cheeks stay matte. Years against an armrest have worn his cuffs pale."
