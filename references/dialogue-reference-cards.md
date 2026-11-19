# Dialogue Reference Card Library

Retrieve according to the activation conditions in the [Dialogue Depth Engine](dialogue-engine.md). Filter by scene purpose first, then rewrite for genre and character DNA. The following 14 cards illustrate creative structures; they are not film/TV quotations, academic sources, or verified performance prescriptions. Example lines are for adapted rewriting only, never direct copying. `prompt_fragment` serves screenwriting/voiceover design and must not be inserted directly into the video body; move complex pauses and subtext as a whole into production notes.

## Subtext: 4 Cards

```json
[
  {
    "id": "SUB-01",
    "source": "Original example: evasion at the doorway",
    "principle": "Use an actionable object to avoid revealing fear",
    "pattern": "When asked about a mental state, answer with the immediate unfinished task",
    "prompt_fragment": "Question: Are you afraid? Answer: The door is still open.",
    "anti_pattern": "The answer is entirely unrelated to objects or goals present in the scene",
    "genre_fit": ["Wuxia", "Crime", "Suspense"],
    "scene_fit": "The exit remains open, the character genuinely needs to hold the door, and fear should not be stated directly"
  },
  {
    "id": "SUB-02",
    "source": "Original example: straightening clothes before parting",
    "principle": "Concrete care carries unspoken attachment",
    "pattern": "Replace an emotional declaration with a reminder concerning an existing object",
    "prompt_fragment": "Button up. It's windy outside.",
    "anti_pattern": "Mechanically apply the line when the scene has no wind or the costume has no buttons",
    "genre_fit": ["Everyday life", "Historical", "Wuxia"],
    "scene_fit": "People who know each other are about to part, and their relationship supports restrained care"
  },
  {
    "id": "SUB-03",
    "source": "Original example: revealing a direction",
    "principle": "A detail someone should not know exposes an information gap",
    "pattern": "Catch the specific noun the other person says despite never having been told it",
    "prompt_fragment": "I never said they were at the north gate.",
    "anti_pattern": "Pretend to catch a slip even though the north gate was explicitly disclosed earlier",
    "genre_fit": ["Suspense", "Crime", "Science fiction"],
    "scene_fit": "The story has established information boundaries, and the character notices the other person letting something slip"
  },
  {
    "id": "SUB-04",
    "source": "Original example: verbal permission to leave",
    "principle": "Speech-action mismatch reveals an unacknowledged wish to keep someone",
    "pattern": "Verbally allow departure while the body still guards the exit",
    "prompt_fragment": "Suit yourself. The speaker's hand still presses down on the door bolt.",
    "anti_pattern": "Introduce controlling behavior without motivation, or change the nature of their relationship",
    "genre_fit": ["Everyday life", "Wuxia", "Suspense"],
    "scene_fit": "The character already wants the other person to stay, and the exit and bolt are physically present"
  }
]
```

## Speech Acts: 3 Cards

```json
[
  {
    "id": "ACT-01",
    "source": "Original example: directing attention to the hand",
    "principle": "Probe what the other person protects and induce them to reveal a choice",
    "pattern": "Point out a visible habit and wait for correction or concealment",
    "prompt_fragment": "You keep protecting that hand.",
    "anti_pattern": "Dialogue discovers a secret from nowhere when no protective action appears in the image",
    "genre_fit": ["Wuxia", "Crime", "Hot-blooded action"],
    "scene_fit": "A hand-protecting action genuinely occurred earlier; the speaker is probing, not omniscient"
  },
  {
    "id": "ACT-02",
    "source": "Original example: conditional passage",
    "principle": "Turn intimidation into an executable conditional exchange",
    "pattern": "One clear condition in exchange for a promise that can currently be kept",
    "prompt_fragment": "Put down the key, and I'll move away from this door.",
    "anti_pattern": "The promise exceeds the character's control, or fulfillment of the condition cannot be seen",
    "genre_fit": ["Crime", "Science fiction", "Suspense"],
    "scene_fit": "The key is an established objective, and the speaker genuinely controls the exit"
  },
  {
    "id": "ACT-03",
    "source": "Original example: getting a companion moving first",
    "principle": "Reassurance works through concrete action instructions",
    "pattern": "A short instruction followed by an action the speaker can undertake",
    "prompt_fragment": "Watch the steps. I'll help you across.",
    "anti_pattern": "The speaker claims to be supporting someone while holding weapons in both hands or standing elsewhere",
    "genre_fit": ["Everyday life", "Historical", "Hot-blooded action"],
    "scene_fit": "A companion hesitates, and their distance and free-hand availability permit physical support"
  }
]
```

## Genre Dialogue: 7 Cards (Original 3 + 4 Textures)

```json
[
  {
    "id": "GEN-01",
    "source": "Original example: a wuxia debt",
    "principle": "An established old object carries an unsettled relationship",
    "pattern": "Mention the object instead of the emotion; action completes the meaning",
    "prompt_fragment": "Here's your sword back. We're not even yet.",
    "anti_pattern": "Invent an old debt, an experience of borrowing a sword, or a revenge relationship",
    "genre_fit": [
      "Wuxia",
      "Historical"
    ],
    "scene_fit": "Both the weapon's return and the unresolved relationship are established in the story"
  },
  {
    "id": "GEN-02",
    "source": "Original example: science-fiction permissions",
    "principle": "Technical words must change the immediate choice",
    "pattern": "Provide a limited permission while pointing out its direct consequence",
    "prompt_fragment": "I can open the door. I can't close it a second time.",
    "anti_pattern": "Change device rules on the spot for a line, or explain the system's history at length",
    "genre_fit": [
      "Science fiction",
      "Suspense"
    ],
    "scene_fit": "Door-control limitations are established, and the characters must use them to decide the evacuation order"
  },
  {
    "id": "GEN-03",
    "source": "Original example: a keyword echo in hot-blooded action",
    "principle": "The same short line gains a new meaning after action changes",
    "pattern": "Earlier the protected person hears it; later they actively say it",
    "prompt_fragment": "This time, follow me.",
    "anti_pattern": "Use repetition alone to create an illusion of growth without a change in ability or choice",
    "genre_fit": [
      "Hot-blooded action",
      "Wuxia",
      "Everyday life"
    ],
    "scene_fit": "A prior leadership relationship exists, and this scene credibly transfers responsibility"
  },
  {
    "id": "GEN-04",
    "source": "Structural example: taking over the power to define in an assertion of authority",
    "principle": "Refuse to prove oneself within the other person's frame; take over the right to rule",
    "pattern": "The other person denies qualification; the character takes over the definition and escalates layer by layer",
    "prompt_fragment": "You ask what I amount to—now let me tell you. What you dare not handle, I will. What you cannot handle, I have even more reason to handle.",
    "anti_pattern": "Overpower through volume alone without taking over the definition or escalating; copy the example or invent authority",
    "genre_fit": [
      "Historical political intrigue",
      "Wuxia",
      "Crime"
    ],
    "scene_fit": "The other person first denies qualification, and the character has an established source of authority; rewrite the example for current authority and available action openings"
  },
  {
    "id": "GEN-05",
    "source": "Structural example: caring phrasing in soft-spoken menace",
    "principle": "Wrap a threat in caring phrasing and replace generic threats with specific details",
    "pattern": "A small verifiable fact makes the other person realize they have been seen through",
    "prompt_fragment": "Your tea has gone cold. Shall I get you another cup—or is the person you're waiting for not coming?",
    "anti_pattern": "Write I'll kill you directly; specific details, an absent person, or knowledge that they will not arrive lack a basis",
    "genre_fit": [
      "Suspense",
      "Crime",
      "Historical political intrigue"
    ],
    "scene_fit": "The tea, awaited person, and speaker's basis for knowing they cannot arrive are all established, and no physical attack is needed here; otherwise rewrite"
  },
  {
    "id": "GEN-06",
    "source": "Structural example: the oblique answer in ironic probing",
    "principle": "Apparent agreement/request for guidance is actually denial/pressing a question",
    "pattern": "Expose the other person through a contradiction in their words",
    "prompt_fragment": "You're right, the north gate is safest. Then why did you come from the south?",
    "anti_pattern": "Explain the irony; make every sentence barbed; leave direction and approach route unestablished",
    "genre_fit": [
      "Suspense",
      "Crime",
      "Historical political intrigue"
    ],
    "scene_fit": "Neither side shows their cards; the north-gate assessment, southern approach, and corresponding information gap have been established"
  },
  {
    "id": "GEN-07",
    "source": "Original structural example: a monologue understating a past event",
    "principle": "A specific small incident carries unstated emotion, without added explanation",
    "pattern": "An established past incident + one understated sentence + no explanation",
    "prompt_fragment": "You saved me half a bowl of porridge that time. I said it was cold and didn't eat it. Afterward, I could never bring myself to throw that bowl away.",
    "anti_pattern": "Say only that a sentence mattered without identifying the past incident; directly explain regret or pain; invent experience",
    "genre_fit": [
      "Everyday life",
      "Wuxia",
      "Suspense"
    ],
    "scene_fit": "The speaker is alone or addressing someone absent; the saved-porridge incident, bowl, and attachment that explains keeping it have a basis. Otherwise use a small incident established in the project"
  }
]
```

## Retrieval and Placement

Check facts with `scene_fit` and narrow style with `genre_fit`; take the most relevant 1–3 cards as alternatives at a time, without forcing in all 14. Transfer the speaking strategy; characters, props, and secrets must come from the current project. Dialogue text, subtext analysis, and stress go into production notes. Visible hand positions, eyelines, and action reactions pass a load check before entering internal G units. Final plain text removes labels and adds character prefixes as usual; card IDs do not enter the body.
