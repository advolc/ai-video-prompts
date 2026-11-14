# Action Modes: pacing and choreography routed by context

`choreography.md` holds the universal physics: choices, weapon logic, force and support, distance, contact. It does **not** say how a fight should *flow*. A desperate last stand, a stealth takedown, and a sparring match are different kinds of scene, with different rhythms, different rules about pauses, and different ways to fail. Pick the mode from the Context Profile (`core/context-routing.md`), then use the physics in `choreography.md` inside it.

The closed exchange (attack, block, step back, reset) is the **duel** mode only. In other modes it reads as polite turn-taking and should be replaced.

Numbers below are starting points for a short-clip workflow. Test them on your model (`evals/cases.md`).

**Where the fighters go** (arena, 3D position ledger, footwork, the line-break rule) is decided in `references/spatial-tactics.md` and is mandatory before any exchange is written. Each mode has a spatial signature there (section 6).

## 1. Parameters every mode defines

| Parameter | Meaning |
|---|---|
| **Rhythm shape** | The tempo curve: bursts and lulls, steady pressure, a single peak, collapse |
| **Tier A density** | Independent interactions per ~5 s of runtime (replaces the old universal "about 3") |
| **Initiative** | Who owns the fight, how it changes hands, and what causes the change |
| **Pause legitimacy** | When a separation or stand-off is allowed. **Resets are legitimate only if the mode or the fatigue state makes them meaningful** |
| **Spatial signature** | How the mode occupies the arena: arcs, a shrinking radius, one clean line in, prescribed marks (`references/spatial-tactics.md` section 6) |
| **Fatigue behavior** | How stamina changes tempo and precision over the scene |
| **Camera stance** | Observer, participant, or subjective (see `references/camera-and-rhythm.md`) |
| **Sound strategy** | Silence versus density, what is heard |
| **Fail-state (story)** | What losing looks like for each side |
| **Fail-state (generation)** | How the clip typically goes wrong in this mode |
| **Splitting** | How to divide into clips |

## 2. The modes

**1. Duel of equals (reading and feints).** *Purpose:* decide a skill contest; reveal character through style. *Rhythm:* probe, burst, lull, burst; lulls carry information (a changed grip, a foot shift). *Density:* 1–3. *Initiative:* alternates, with cause (a feint works, a habit is exploited). *Pauses:* legitimate when the character changes something or reads something. *Fatigue:* mild; shows in the second half. *Camera:* mostly observer, closing in at decisive crossings. *Sound:* breath and steel; silence in lulls. *Story fail-state:* a misread. *Generation fail-state:* **the reset loop**, where every exchange looks the same. *Splitting:* by exchange pairs.

**2. Desperate last stand.** *Purpose:* show courage and cost; protect something. *Rhythm:* sustained pressure with shrinking recovery; moments of a lull are stolen, not granted. *Density:* 2–4 with **overlap** (the next attack starts before the last resolves). *Initiative:* held by the attackers; the defender only reacts, then makes one desperate move. *Pauses:* **not legitimate** unless a hit forces one. *Fatigue:* dominant: guard sinks, footwork shortens, breath breaks, grip changes, improvised weapons appear. *Camera:* participant, close and unstable. *Sound:* ragged breath, impacts, fabric. *Story fail-state:* collapse or being overrun. *Generation fail-state:* **a clean duel in disguise**, where the defender never visibly tires. *Splitting:* chained clips; the state seam carries stamina and injury.

**3. Stealth takedown or assassination.** *Purpose:* competence and menace; one decisive act. *Rhythm:* long approach, a single contact, aftermath. *Density:* **0–1 total per clip.** *Initiative:* the assailant, absolute. *Pauses:* waiting is the scene. *Fatigue:* none; control of breath instead. *Camera:* long lens from distance, then close on the decisive hands; minimal movement. *Sound:* near silence; one controlled sound (a boot on gravel, a breath). *Story fail-state:* **noise or discovery.** *Generation fail-state:* a flurry of blades where one contact was meant. *Splitting:* one unit; do not split the approach from the strike.

**4. Sparring and training.** *Purpose:* teaching, play, bonding, or measuring. *Rhythm:* exchanges, then stops to correct; safe contact. *Density:* 1–2. *Initiative:* the stronger one lets the other attack. *Pauses:* **legitimate and expected** (a correction, a grin, a repositioning). *Fatigue:* shows in sweat and breath. *Camera:* observer, relaxed; closer on the instruction beats. *Sound:* wooden or padded impacts, casual speech. *Story fail-state:* injury by accident, or one pushing too far. *Generation fail-state:* the clip reads as lethal combat. *Splitting:* by teaching beat.

**5. Ambush and surprise.** *Purpose:* shock; establish threat. *Rhythm:* a front-loaded burst, then scatter or regroup. *Density:* 3 or more in the first 2 s, then 1–2. *Initiative:* the ambusher at first; chaos follows. *Pauses:* none in the burst; legitimate during the scatter. *Fatigue:* adrenaline, no stamina loss yet. *Camera:* participant; a whip or a sudden entry. *Sound:* silence snapping into noise. *Story fail-state:* the victim is overwhelmed or escapes. *Generation fail-state:* the ambusher is announced (a telegraphed run-up). *Splitting:* burst as one unit, aftermath as another.

**6. Overwhelming dominance (one-sided).** *Purpose:* show power gap, cruelty, or economy. *Rhythm:* efficient, unhurried; the weaker side's attempts fail quickly. *Density:* 1–2. *Initiative:* never shifts. *Pauses:* the dominant can hold a lull to show contempt. *Fatigue:* only the weaker side tires. *Camera:* observer, often lower on the dominant, higher on the victim. *Sound:* low and spare. *Story fail-state:* the dominant's single misjudgment. *Generation fail-state:* both sides look equally skilled.

**7. Flight fight (retreat under pressure, chase with contact).** *Purpose:* get away or reach something; fighting is an obstacle. *Rhythm:* movement-first, with brief contacts that cost time. *Density:* 1–2, interleaved with locomotion. *Initiative:* the pursuer; the fugitive makes tactical choices (terrain, objects). *Pauses:* none; any stop is a cost. *Fatigue:* builds through the chase. *Camera:* tracking, a participant at the fugitive's pace. *Sound:* footfalls, breath, environment. *Story fail-state:* being caught or cornered. *Generation fail-state:* the chase stops so the fight can happen. *Splitting:* by terrain segment.

**8. Brawl (street fight, mutual exhaustion).** *Purpose:* messy, human conflict. *Rhythm:* grappling, wild swings, clinches, breaks forced by exhaustion. *Density:* 2–3, ragged. *Initiative:* swings back and forth by luck as much as skill. *Pauses:* **exhaustion pauses are legitimate** (hands on knees, spitting, circling). *Fatigue:* dominant and visible. *Camera:* participant, close, handheld. *Sound:* grunts, clothes, impacts, onlookers. *Story fail-state:* one quits, or an outside intervention. *Generation fail-state:* choreographed elegance.

**9. Group melee and siege.** *Purpose:* scale and chaos. *Rhythm:* waves; one clear line through the mass. *Density:* one main exchange plus background. *Initiative:* by group position; the lead fighter's local initiative. *Pauses:* none for the group; individuals get stolen moments. *Fatigue:* the lead's fatigue is the clock. *Camera:* wide to establish, then a participant on the lead. *Sound:* layered crowd. *Generation fail-state:* background figures freeze or all attack one at a time. See `choreography.md` (zoning).

**10. Ritual or code-bound duel.** *Purpose:* honor, ceremony, tradition. *Rhythm:* formal opening, restrained exchanges, silence. *Density:* 0–2. *Initiative:* by the code (who may strike first). *Pauses:* **meaningful and prescribed.** *Fatigue:* hidden by discipline. *Camera:* symmetrical, wide, locked. *Sound:* near silence, one ritual sound. *Story fail-state:* **a breach of the code.** *Generation fail-state:* it reads as an ordinary fight.

## 3. Cross-mode grammar (use as the mode calls for it)

- **Initiative ledger:** one line per beat of who holds initiative and why it moved. A fight with no initiative change is a demonstration; one with a cause-driven change is a story.
- **Pressure gradient:** pressure is shown as space given up: steps back, terrain lost, the defender's options narrowing. Record start and end positions as (x, y, z) in the position ledger, not only as a distance; pressure that moves along one line is weaker than pressure that curves the defender around terrain.
- **Overlap:** where the mode calls for it, a strike begins while the previous one is still resolving ("the left blade is already sweeping in as the first block slides it away").
- **Consequence accumulation:** each hit, miss, or loss of terrain leaves a trace that changes the next move (a cut strap, a jarred arm, a slipped foot, a cracked wall). A trace that never matters is decoration.
- **Reset test:** if two consecutive beats begin from the same positions **or the same bearing and height**, the mode has stalled. A fight that oscillates along one line fails the line-break rule in `references/spatial-tactics.md` even though its positions differ. Allow it only where pause legitimacy says so.
- **Failed attacks matter:** a miss that bites a wall, throws the attacker off balance, or opens him up is worth more than a clean block.
- **The ending is a result:** the final state must follow from the fight. Positions differ from the opening and the difference is explained.

## 4. Fatigue routing

| Stamina | Visible effects |
|---|---|
| Fresh | Full range, high guard, long steps, controlled breath |
| Winded | Shorter steps, slightly lowered guard, visible breath, a delay before counters |
| Spent | Guard sinks, steps drag, grips adjust, recoveries incomplete, a hand to knee or wall, attacks telegraph |
| Injured | The injured limb changes stance and route; the character protects it and loses options (see the state ledger) |

Fatigue changes tempo and precision; it never changes purpose (core rule 2). Exhaustion can **legitimize** a pause in brawl and last-stand modes.

## 5. Reach routing

| Pairing | Pacing consequence |
|---|---|
| Long vs short | The long weapon wins distance, the short wins inside. Pacing is a fight for range: retreat to open it, close to spoil it. A closing attempt is a moment of risk |
| Equal reach | Reads and feints; initiative changes by timing |
| Armed vs unarmed | The unarmed fighter works angles and grabs; the armed one controls distance. Contact is costly for the unarmed |
| Ranged vs melee | A race against the closing distance; cover and terrain matter more than exchanges |
| Improvised weapons | Brief, awkward, not skilled; the object's weight and shape limit moves |
| Size or speed mismatch | The larger overpowers on contact; the smaller wins by evasion and terrain. Show the difference in the first contact |

## 6. Environment routing

| Environment | Effect |
|---|---|
| Confined (corridor, doorway) | No flanking; one line of attack; wall strikes; short weapons favored |
| Open | Circling, flanking, retreat room; use of the whole frame |
| Vertical (ledge, stairs, roof) | Height advantage; falling is a fail-state; footing governs every step |
| Slippery or loose ground (ice, gravel, mud) | Footing errors become events; slides and stumbles carry consequences |
| Crowded | Collateral blocking, hostages, limited swing room |
| Dark or low visibility | Sound and touch lead; light sources become tactical |
| Moving platform (horse, boat, vehicle) | Balance and momentum come first; the platform's motion is part of every attack |

## 7. Routing procedure

1. Read the Context Profile.
2. Pick the mode by **purpose** (section 2). If two seem to fit, choose the one that matches the story's fail-state.
3. Set the Tier A density and splitting for the mode.
4. Write the arena card and the position ledger (`references/spatial-tactics.md`), then apply fatigue, reach, and environment adjustments.
5. Write the initiative ledger and the consequences that accumulate.
6. Write the ending as a result.
7. Note the mode's generation fail-state in the design record, to speed triage.

## 8. Worked routing (illustrations)

| Profile | Mode | What changes |
|---|---|---|
| A wounded guard holding a door against a squad, night | Last stand | Overlap, sinking guard, no clean resets, consequence accumulation, ends with collapse or a held line |
| An assassin and a sleeping target | Stealth | One approach unit, silence, a single contact, aftermath |
| Master and student in a courtyard | Sparring | Stops to correct, light contact, a playful lull, a final touch |
| Two exhausted rivals in a market alley | Brawl | Clinches, spitting, hands on knees, wild swings |
| Two rival swordsmen, formal challenge | Ritual duel | Formal bow, restrained exchanges, silence, a breach as the turn |
