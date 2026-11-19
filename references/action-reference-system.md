# Action Reference Card System

Use this module to turn existing references or established actions into visible paths, support, and contact for the current scene. When an action has an execution gap, or the user requests reference analysis, use the relevant cards as needed; do not wait for an additional module to be enabled, or load the whole library merely because the request says “intense.” Follow [source scope](source-scope.md) for the evidence boundaries of references.

## Action reference card JSON fields

```json
{
  "id": "ACT-EXAMPLE-01",
  "source": {
    "type": "original_design",
    "title": "Original straight-punch visual breakdown example",
    "locator": "Example in this file; no particular athlete or film is cited",
    "evidence": "Choreographic hypothesis; not validated through live-action movement or generated video"
  },
  "domain": "Boxing force production",
  "principle": "Support, torso rotation, and post-strike recovery need continuity",
  "action_patterns": ["Rear foot pushes against the ground", "Hips and shoulders turn toward the target", "Fist retracts after touching the target"],
  "style_tags": ["Realistic", "Brief", "Readable from the side"],
  "exaggeration": "Extend only the sleeve's follow-through; body support follows this scene's setup",
  "prompt_fragment": "The ball of the right foot pushes against the ground; the right hip turns forward, and the right shoulder carries the right fist along a straight path toward the opponent's chest. After the knuckles touch, the right arm retracts and the center of mass settles between both feet.",
  "anti_pattern": "The arm extends and retracts alone while the torso instantly crosses the original distance",
  "scene_fit": {"distance": "Within reach of the chest", "ground": "Weight-bearing ground", "camera": "Side medium shot", "exclude": "The current supporting foot is injured, or the body is airborne with no source of thrust"}
}
```

`id` is for retrieval only; `principle` explains the idea; `prompt_fragment` is a candidate for adaptation, not an entire final input ready for direct reuse. At minimum, `source` distinguishes user-supplied material, verified primary material, and original hypotheses; state the file/link, page/timecode, and evidence boundary. Without viewing the original footage or finding the material, do not invent real schools, actors, coaches, or attributions. An original card must not be described as a finding from live-action instruction.

## Reference source categories

| Category | Retrieval focus | Observations worth recording | Adaptation checks |
|---|---|---|---|
| Boxing force production | Support, punch path, guard, recovery | Which foot pushes, and how hips, shoulders, and fist connect | Effective reach, handedness, ground friction |
| Kickboxing / Muay Thai | Kicking support, hip rotation, close range | Supporting-foot placement, knee/shin travel and return | Space clearance, clothing/armor restrictions, opponent response |
| Sanda / traditional Chinese martial arts | Advance/retreat, interception, short strikes, rhythm | Limbs and contact actually visible in the reference | Do not substitute a school name for an action or generalize across all schools |
| Wrestling / grappling | Grips, imbalance, pivots, landing | Where hands grip, what the center of mass crosses, how the body lands | Validate complex grips in phases; preserve identity and limb count |
| Weapons | Grip, striking surface, blade line, recovery | Which part of the weapon meets what | Length, rigidity/flexibility, grip spacing, interpenetration, clearance |
| Screen fight choreography | Attack/defense intent, camera, spatial illusion | How observed action and editing divide the work | A cheated screen hit is not proof of real mechanics |
| Animation drawing | Anticipation, key poses, exaggeration, recovery | Silhouette, speed changes, follow-through direction | Recheck support and joints when translating to 3D; do not copy deformation directly |
| Biomechanics | Momentum, center of mass, support, load | Subjects and conditions of verified primary research/data | Do not invent numbers or treat group research as exact parameters for this character |

For factual material, prioritize user material and verifiable primary instruction, original footage, creator analysis, or research. Verify sources first when uncertain about a specialist fact. Without retrieval tools, mark the reference “pending verification”; clearly labeled original choreography candidates remain possible, but do not pretend retrieval has been completed.

## Retrieval pipeline: parse → tag → retrieve → adapt → place

1. Parse the task: extract the main action's goal, both starting positions, weapons/hand positions, ground support, outcome, and camera conditions; freeze the user's established signature moments.
2. Tag distance, contact target, support, speed character, stylistic exaggeration level, and scene clearance. Find the action gap first; do not add moves to fill a card.
3. Retrieve 3–5 candidate cards: these are internal candidates, not a requirement to put them all in one segment. Honestly provide fewer when material is limited; do not invent sources to meet a count. Show only the most relevant differences.
4. Adapt: rewrite for the characters' current left/right, handedness, weapons, injuries, materials, and camera; choose one primary plan. Reject cards that do not fit and record why.
5. Integrate into the internal design record: merge/select `prompt_fragment` material along the same causal chain; use `anti_pattern` to check the most relevant current failure risk, without carrying old template labels into the prose. Preserve independent events individually, checking duration, contact, and simultaneous demands through [generation handoff](generation-handoff.md). Card count is not an action allowance and does not automatically determine request splitting.
6. Transcribe semantically before output: remove terminology, card IDs, and labels from the body; turn prohibitions into positive visible conditions; integrate character/setting prefixes with the segment's action into self-contained plain prose. Put sources, adaptation reasons, and validation status in production notes.

## Principle → wording map

These demonstrate choreographic wording. Match the character's posture before using them; they do not require every action to use the same force-production sequence.

| Design term | Candidate visible wording | Conditions that cannot be omitted |
|---|---|---|
| Kinetic chain | The ball of the rear foot pushes against the ground; the hips turn toward the target first, and the shoulder carries the arm forward | Which foot can bear weight; where the hand makes contact |
| Lowered center of mass | Both knees bend, the pelvis lowers, and the torso remains within the support of both feet | Do not turn lowering into kneeling or an unsupported fall |
| Whole-body coordination | The supporting foot plants firmly, hips and shoulders turn in the same direction, and the palm heel pushes toward the target | Replace terminology with visible limb relationships while preserving distinctions in the original technique |
| Yielding / redirecting force | The forearm meets the incoming fist obliquely; the torso turns sideways along the incoming force, guiding the punch outside the body | Contact occurs first; support permits rotation |
| Imbalance | The shoulder on the pulled side moves outside the base of support first, then the foot on that side steps out to catch it | Make the grip and trigger explicit; no uncaused flying fall |
| Anticipation and burst | The right shoulder draws back briefly; after the right foot plants, the arm drives quickly forward along the established path | Do not add a second wind-up attack |
| Laban effort: heavy / direct / sudden | Elbow close to the torso, front foot firmly planted, the fist shoots out on a short straight path | Keep terminology in design notes; “heavy” does not make every movement slow motion |
| Animated follow-through | After the body stops, the hem continues swinging in the original direction before settling | The hem is not the sole evidence of a hit |

## Integration and validation boundaries

Cards assist design and stay out of final prompts. At the end of each use, retain only a short summary: “selected card/source, visible action, start/end states, risks to test”; the entire library need not be reread later. Body detail belongs to Tier B, not additional Tier A events. When it competes with existing action, use it to replace ambiguous wording rather than stack on another move. When a test clip fails, follow the [AI pipeline](ai-pipeline.md) to find the earliest failure instead of adding more terminology.
