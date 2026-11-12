# v3 Extended Examples

Three illustrative Extended prompts. **None has been run on a video model.** Characters, props, and facts are invented for the examples and do not transfer to any project. Each copy block passes `scripts/lint_prompt.py`.

## Example 1: Power dialogue (English)

**Inputs from the user:** An office study, late afternoon. Chen is Wu's superior. Wu reports that a shipment failed customs. Chen should not raise his voice. Outcome: Wu finishes his sentence steadily; Chen lets him.

**Design record (internal, not in the prompt):**
- Locked: Chen superior, Wu subordinate; shipment failed customs on Tuesday; Chen stays calm; Wu ends steady.
- Added texture: porcelain cup and saucer for Chen; tungsten desk lamp; window light; dust in the beam.
- Status ledger: Chen high, Wu low. Chen widens the gap with silence. Wu makes a small claim at the end.
- Dialogue: Wu's stammer is anxiety; Chen's echo "Tuesday." is the pressure move.
- Beats: see `lens/body-and-status.md` section 9.

**Copy block (Extended):**

> Live-action drama, 16:9. Shot on a 85 mm lens with shallow depth of field, 35 mm film character with fine grain, warm tungsten palette and deep, dense shadows, natural motion blur, locked-off with one slow push-in.
>
> Chen is in his mid-fifties, heavy-lidded, with grey stubble that thins along the cheekbones; deep lines run from his nose to the corners of his mouth, and the skin under his eyes is slightly dark, with one faint blue vein. His left brow sits a little higher than his right. He wears a charcoal wool jacket, rubbed pale at the cuffs where his forearms rest, and a white shirt with a collar that has softened with washing. Wu is in his early thirties, narrow-faced, with a faint flush rising along his neck, short black hair with a few strands lifting at the crown, a grey suit creased across the lap, and thin fingers with ridged nails.
>
> A study at late afternoon: a heavy desk, a worn leather armchair, a wooden visitor's chair, shelves of ledgers. A low tungsten desk lamp throws amber light across Wu's lower face from the left, its steep falloff dropping his right cheek into shadow; cool grey window light behind Chen rims his silver hair, and a small window-shaped highlight shows in each of his eyes. Dust turns slowly in the window beam.
>
> Chen sits far back in the armchair, right ankle over left knee, a porcelain cup balanced on his knee. Wu perches on the front third of the wooden chair, palms flat on his thighs. Wu swallows, then says, voice thin and fast, "Sir, the shipment, it, uh, it didn't clear customs on Tuesday." Chen says nothing. His thumb turns the cup a quarter-turn on its saucer. Wu's left hand slides to his cuff and tugs. The camera begins its slow push-in on Chen's face. Chen lifts the cup, the lid ticks once against the porcelain, and he sips with his eyes on Wu over the rim, his expression flat and patient. He sets the cup down with a small click and lets the silence run. "Tuesday," he says, low and unhurried, his voice falling at the end. A thread of steam bends toward Wu. For an instant one corner of Chen's mouth tightens and lifts, then his face goes blank again. Wu's palms stay flat; he takes one slow breath through his nose and says, level, "Tuesday. Yes, sir. The paperwork was filed late, and I should have caught it." Chen's ankle changes sides; the lamp light slides along his polished shoe.
>
> The room is quiet except for the tick of the cup and a distant clock; Chen's voice sits low and dry, Wu's a little breathy. The shot ends on the two of them in the same chairs, Chen's cup half empty on his knee, Wu's palms flat on his thighs, the lamp's amber on Wu's chin and the grey window light on Chen's hair.

**Added-texture note (outside the block):** Added: porcelain cup and saucer, tungsten desk lamp, window light with dust, wool jacket details, and Wu's cuff tug as his self-touch. Assumptions: modern workplace and period unspecified; no native speech verified (voice script below).

**Voice script (outside the block):**
```
Speaker | Line | Delivery | Pause
Wu | "Sir, the shipment, it, uh, it didn't clear customs on Tuesday." | thin, fast, a stammer on "it" | 0.3 before
Chen | "Tuesday." | low, unhurried, falling | 0.8 before
Wu | "Tuesday. Yes, sir. The paperwork was filed late, and I should have caught it." | level, a short inhale first | 1.0 before
```
*Pauses are estimates; read aloud before relying on them.*

**What the lint sees:** a few modal words ("should have caught it") appear inside a quoted line and are fine.

## Example 2: Action with a seam (Chinese)

**Inputs:** 雪夜，旧塔门口。林握短杖守门，韩持长矛。林左前臂有伤，不能暴露。韩一刺，林架开并近身，韩退半步。结果：不分胜负。

**设计记录（内部）：** 锁定：林左前臂伤、短杖、长矛、不分胜负。新增质感：雪、呼出白气、门边灯笼、杖上的包浆。事件层（A）：刺—架—近身—退，一条接触链。表演层（B）：林左手藏袖、呼吸浅而平；韩目光落在她的袖口。质感层（C）：灯笼琥珀光、冷蓝环境、粗颗粒、窄快门。

**可复制文本（扩展版）：**

> 写实电影质感，16:9。35毫米镜头，手持带呼吸感，窄快门使动作清脆利落，35毫米胶片的中等颗粒，灯笼周围有淡淡的高光光晕，冷蓝与琥珀的色调，暗部压得厚重，黑色里保留粗布的纹理。
>
> 林三十出头，脸窄，右眉略高于左眉，鼻尖和耳缘被冻得发红，嘴唇干裂、左嘴角有一道小口子；短发束在脑后，几缕碎发被风掀起；一身灰色旧棉袄，肘部压出扁平的棉线，左袖口垂得很长、被手磨得发白；右手握一根短铁头木杖，木纹被掌心磨得发亮。韩四十岁上下，高个，下颌胡茬粗短、杂着灰白，眼下有一道旧痕，灰色旅行外套，肩头积着雪，双手握一杆长矛，矛杆深色，握持处磨得发暗，矛尖蒙着一层薄油。
>
> 夜里的旧塔门口，石阶覆着薄雪，门框边挂着一盏灯笼，琥珀色的光落在门槛和林的右脸颊上，背景是冷蓝的雪夜，雪片从光里斜斜落下。两人每次呼气都留下一团白气，灯笼的火苗被穿堂风吹得微微偏向左侧，影子随之轻轻摆动。林的眼睛里有一个小小的灯形亮点。
>
> 林站在门里，重心压在右腿，左手缩进袖子，门闩斜靠在她右肩上，呼吸又浅又平。韩站在一矛之外，目光落在她的左袖上，长矛低垂在身前，他的呼气在冷空气里拉得很长。韩先把矛尖抬起半寸，随即向她胸口直刺。林的右手把短杖横过矛杆，向身体左侧一扫，矛尖滑过她原来胸口的位置；杖头压住矛杆后，她右脚向前一步，杖身与右肩一起顶上韩的胸口。韩的胸口先陷了一下，随后向后退出半步，膝微屈稳住脚，矛从身前收回。镜头随林的这一步向前微微跟推，在接触的一刻稳住，雪片在镜头前掠过。林停在原地，左臂仍藏在袖中，右手握杖，呼吸依旧又浅又平。
>
> 雪落在石阶上的声音很轻，木杖与矛杆碰撞发出一声短促的闷响，灯笼的灯绳在风里轻轻磕着门框。画面最后停在林站在门里、门开在她身后、韩在一矛之外收着长矛，雪继续落在两人之间，灯笼的琥珀光在林的脸颊上微微晃动。

**备注（块外）：** 新增：灯笼、呼出白气、杖上的包浆、雪。假设：未核实原生音频。

## Example 3: Face close-up (English, protect the user target)

**Inputs:** The user demands a close-up of Lin hiding fear when Han names her wound.

**Design (internal):** Mask: calm and level. Leak: one swallow and a flicker at the brows. Keep the fight out of this clip.

> Live-action drama, 16:9. Shot on an 85 mm lens with shallow depth of field, 35 mm film character with fine grain, a faint halation around the lantern's flame, cool blue ambient with a warm amber edge, dense shadows that keep the weave of her collar, locked-off with a very slow push-in.
>
> Lin is in her early thirties, narrow-faced, her right brow set a little higher than her left, short black hair tied back with a few strands loosened by wind and beaded with melting snow; fine lines gather at the corners of her eyes, a faint blue vein shows under the lower lid, and the cold has reddened the tip of her nose and the rim of each ear, which glow faintly warm where the lantern catches them. Her lips are dry, with a small split at one corner. She wears a grey padded jacket with the collar rubbed pale, snow melting into dark spots on the shoulder.
>
> Han stands just out of focus in the foreground, the edge of his grey travel coat and a hand gripping a spear shaft softly blurred, and the stone doorway behind Lin shows a worn threshold under a thin layer of snow. Snow falls through cold blue air; a lantern at the camera's right throws a warm edge across her cheek and jaw, its flame leaning slightly in the draft, and a small lantern-shaped highlight sits in each of her eyes. Each exhale leaves a pale puff in front of her face.
>
> She looks at Han's face, her expression level, her breath shallow and even. When Han says her name, her upper lids lift a hair and her brows draw together for an instant; her lips press into a thin line, her throat moves in one swallow, and a pulse ticks at her neck. Then her face smooths into a calm, patient blankness, and her eyes drop for a moment to Han's hands before returning to his face. The camera's push-in has barely moved when Han speaks again, and a snowflake lands on her lashes and melts. Her gaze holds steady on him.
>
> The night is quiet except for the soft tick of snow on stone and the faint creak of the lantern's cord. The shot ends on Lin's face holding still, the lantern's amber on her cheek, the cold blue behind her, and a single snowflake settling on her shoulder.

**Why the face beat is one flicker plus a mask:** a single small leak (brows and swallow) keeps the beat readable; a stack of leaks would blur. If the model cannot render the flicker, fall back to gaze and head turn (`lens/face-pass.md` section 7).

## Before and after: the v1 problem

**v1-style output (analytical):** "A and B face each other. A, the superior, shows composure through a calm, unhurried posture; there is tension between them. A does not interrupt and does not move. Only after B finishes speaking does A respond. No new action is added in this clip."

**v3 output (execution):** see Example 1. The superior sits back, ankle on knee, cup balanced; the cup turns, lifts, ticks, and lands; his silence runs; the subordinate perches and swallows. Every sentence is something a camera or microphone would capture.

## Compact tier (same scene, for "short/lite")

> Live-action drama, 85 mm, shallow depth of field, warm tungsten, fine grain. Chen, mid-fifties, grey stubble, charcoal jacket, sits far back in a leather armchair, ankle over knee, a porcelain cup on his knee; Wu, early thirties, grey suit, perches on the front of a wooden chair, palms on his thighs. Wu says, thin and fast, "Sir, the shipment, it, uh, it didn't clear customs on Tuesday." Chen lifts the cup, sips with his eyes on Wu, sets it down with a click, and says low, "Tuesday." Warm lamp on Wu's chin, grey window light on Chen's hair. The shot ends on both still in their seats.
