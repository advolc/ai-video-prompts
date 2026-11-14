# Observed clip: 30 s wuxia duel (model not named)

Verified on: 2026-11-12
Source: own test, 1 clip (frame sampling, ffprobe, and the user's listening report). Model and version: **not recorded; fill in**.

## Checklist answers (from this one clip)
1. Duration: a 30.05 s output was produced from a 30 s request.
2. Single or multi-shot: **multi-shot in one generation**. The prompt called for camera cuts and the video shows them.
3. Reference inputs: none used.
4. First/last frame: none used.
5. Native audio: **speech was audible** (the user heard both lines). **Lip sync was judged good enough** for both lines (user report, medium-wide framing). Continuous audio throughout (no silence over 0.4 s). Sound-effect quality not assessed.
6. Prompt language: English worked.
7. Negative field: not used.
8. Camera control: text-only camera language was followed (hoof-level tracking, rise to the rider, cuts, pull-back).
9. Output: 1280x720, 24 fps. The "1080p" in the prompt was **not** honored.
10. Prompt length: a **997-word prompt for 30 s** was followed closely (about 33 words per second).
11. Cinematography vocabulary: used in the look anchor (35 mm spherical, medium depth of field, fine-grain film stock, low saturation, crisp motion blur). Not tested in isolation; the look was photographic, grain faint.
12. Fine face control: faces were small in the dialogue section; the nearest faces (about 6–8 s) looked smooth and slightly beautified.

## Results
What worked: the whole choreography chain, costume and prop details, a near-exact final composition (swordsman low left on gravel, raider high right on the slope), a still end hold, violet blade trails.
What did not: the warm gold stream was not obvious in the sampled frames; skin micro-detail was minimal (the prompt supplied none); a possible small watermark in the lower right around 17 s (unconfirmed).
Open questions: does the model honor skin and face detail when the prompt supplies it? Does the same prompt at half the length drift? Does sync hold at a close shot?
