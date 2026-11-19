# Pass 2: Physical Light and Atmosphere

Evidence: this is a design vocabulary; direct renderer response follows [evidence classes](../models/capabilities.md#evidence-classes). Preserve the craft even when the final prompt uses ordinary visible language.
Name the **source first**, then the emotion. Light that has a place, a direction, a color temperature, and a falloff reads as photographed. Light that is only "dramatic" reads as generated. This pass carries over v1's lighting rules and extends them. 

## 1. Source before mood

- **Natural:** sun, skylight, window, overcast. **Practical:** lamps, fire, candles, screens, neon, headlights, all visible in the scene. **Shaped:** a motivated fill or rim that behaves like one of the above.
- Every light in the prompt has a visible or plausible origin. Do not add a moon, torch, or window just to get a rim; use the sources the scene already has, or adjust brightness between subject and background.
- Mixed light needs a primary and a secondary. Not every object glows.

## 2. Color temperature families (approximate)

| Source | About | Look |
| --- | --- | --- |
| Candle / oil lamp | 1800–2000 K | Deep orange, flicker, tiny pool |
| Sodium street lamp | ~2000 K | Saturated orange, flat |
| Tungsten bulb | 2700–3200 K | Warm amber, cozy to tense |
| Fluorescent | ~4000 K, green cast | Institutional, sickly skin |
| Midday daylight | 5500–5600 K | Neutral white, hard shadows |
| Overcast | ~6500 K | Cool, soft, low contrast |
| Open shade, blue hour | 7000–10000 K | Blue, calm, melancholy |
| Moonlight (as rendered) | reads blue against tungsten | Cool edge light, low intensity |

A shot uses **one family** for the key, with at most one contrasting practical (warm lamp against cool window). Write the contrast as depiction: "cool grey window light on the left half of his face, a warm lamp glow on the desk".

## 3. Direction and modeling

| Position | Visible effect | Risk and fix |
| --- | --- | --- |
| Frontal | Face and cloth read clearly | Flat: separate with background layers |
| Side | Volume, texture, contact surfaces | Keep detail on the dark side |
| Back, rim | Silhouette, rain streaks, hair edge | Do not black out the subject |
| Top | Pressed shoulders, deep eye sockets | Give eyes a natural reflection |
| Under | Unease, threat | Not automatically evil |
| Short or broad | Side of face away from camera lit (short) or toward camera (broad) | Short slims, broad opens |
| Loop, Rembrandt, split, butterfly | Named facial patterns | Always add the depiction ("a small triangle of light on the shadowed cheek") |

## 4. Quality, falloff, fill

- **Hard** light casts a clear shadow edge; **soft** wraps skin; **diffuse** lowers contrast; **cutting** light hits only a zone.
- **Falloff:** a lamp close to a face falls off fast (the near cheek bright, the far cheek dark); a distant window falls off gently. Write which: "the lamp sits close enough that his far cheek drops into shadow".
- **Bounce and negative fill:** warm bounce from a wooden desk onto the chin; black cloth or a dark wall deepening the shadow side. Mention only if it shows.
- **Ratio, in plain words:** "bright on the lit side, the dark side keeps the weave of the coat" beats any number. Exposure protects the face, hands, and blade edge; blacks are dense but never dead.

## 5. Eyes: catchlights

Dead eyes are a classic AI tell. Give the eyes a **catchlight** from a named source: "a small window-shaped highlight in each eye", "a warm point of lamplight". Make them match the key's direction. A faint reflection in the wet of the eye under top light keeps the sockets alive.

## 6. Practicals and living light (v1 rules, kept)

- **Flames:** a bare candle, lamp, or torch breathes if air reaches it: the flame leans, and the shadows shift with it. Sealed shades, stable electric lamps, and still air do not flicker. Do not add a flicker just for "cinema".
- **Space transitions:** when a door opens, say how the existing light cuts across the floor and into the person's face. Keep the key's world direction; no teleport exposure or skin-tone jump.
- **Edge separation in the dark:** use an existing moon, flame, window, or reflection to rim a shoulder or hair; if none exists, lift the background slightly or offer a fill candidate instead of inventing one.
- **Continuity across clips:** record the key's world direction, color family, and brightness. A camera turn changes screen left and right, not the world source.
- **Never** let a flash, glow, or shadow swallow the face, hands, blade, or contact point.

## 7. Atmosphere

| Element | Depict as | Needs |
| --- | --- | --- |
| Haze / mist | Visible shafts, lifted shadows, soft glow around lamps | Established setting |
| Dust motes | Specks drifting in a light beam, turning slowly | A beam and still air |
| Steam | Thin rise from a cup, curling when someone moves | A hot object |
| Smoke | Slow drift following the air | An existing source |
| Breath fog | A pale puff at each exhale | Cold air, around 5 C or colder |
| Rain | Streaks backlit, ripples, wet sheen | Established weather |
| Wet surfaces | Reflections of nearby lights, darker cloth | Rain or recent wet |
| Sweat sheen | Fine shine at hairline, temple, upper lip | Effort or heat |

## 8. Environmental micro-motion

Small, continuous motion makes a scene feel inhabited. It must follow the **established airflow**: one wind direction, one set of air currents.

- Hair flyaways lift in a door draft; a sleeve edge stirs when someone passes; a curtain breathes at an open window.
- A thread of steam bends toward the speaker; dust turns in a beam when a door shuts.
- Water, grass, and leaves answer the same wind as the cloth.
- Motion follows cause: the cloth stirs after the person moves, the dust lifts after the door swings.

## 9. Time-of-day palettes

| Time | Palette |
| --- | --- |
| Golden hour | Low amber sun, long soft shadows, warm skin, rim on hair |
| Blue hour | Deep blue ambient with warm windows |
| Overcast noon | Even soft light, pale shadows |
| Night interior | Pools of practical light, dark corners |
| Dawn | Pale cool light warming at the horizon |

## 10. Light and skin

Skin shows depth when light grazes it: side or three-quarter light brings out pores, lines, stubble, and subsurface glow at ears and nostrils (see `skin-and-material.md`). Flat frontal light and heavy diffusion hide them. Choose the light that matches the skin detail you want.

## 11. Examples

- *Interior power scene:* "A low tungsten desk lamp throws amber light across Wu's lower face from the left, steep falloff dropping his right cheek into shadow; cool grey window light behind Chen rims his silver hair, and a small window-shaped highlight shows in each of his eyes. Dust turns slowly in the window beam."
- *Night exterior:* "Snow falls through the cold blue ambient light; a lantern on the doorpost throws amber light across the threshold and onto Lin's right cheek; each exhale leaves a pale puff in front of her face."
- *Alternate wording:* "Cool grey window light falls on his shoulder from behind and to the left; the tungsten desk lamp leaves a small warm patch on his chin. A window-shaped catchlight appears in each eye, and his breath gently bends the steam above the cup."

## 12. Mood and context routing

Use the single [context-to-look table](optics-and-stock.md#10-routing-the-look-from-context) for creative starting points. This file owns source direction, quality, falloff and material interaction, not a second mood preset system. Existing sources constrain the design: a turn in emotion does not make a lamp dim or a new source appear without an established cause. Render the selected mood through actual source placement, exposure and framing consistent with the scene.
