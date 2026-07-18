# Video Workflow

## Contents

1. Establish the visual system
2. Design the sequence
3. Build production-ready assets
4. Use the motion grammar
5. Direct sound and subtitles
6. Generate, composite, and inspect
7. Reusable sequence brief

## 1. Establish the visual system

Create or approve a representative style frame before producing the whole sequence. It must settle:

- aspect ratio and safe areas
- paper stock and primary ink
- accent color limits
- headline and subtitle hierarchy
- halftone scale and defect strength
- shadow density and atmospheric visibility
- the balance between photography, engraving, and collage

For multiple shots, carry forward a compact continuity block containing palette, paper, print process, lens/shot behavior, lighting logic, and negatives. Keep characters, clothes, props, architecture, weather, and time of day consistent.

## 2. Design the sequence

Give every beat an editorial role:

- **Headline:** establishes the central image or claim.
- **Evidence:** reveals object, detail, location, archive, or consequence.
- **Turn:** changes meaning through a cut, reveal, occlusion, or light shift.
- **Imprint:** ends on a memorable mark, line, or quiet hold.

Suggested pacing:

- **About 5 seconds:** one idea, two or three beats, one reveal, one final hold.
- **10–20 seconds:** three to five shots with a single visual argument.
- **30–60 seconds:** organize into short editorial paragraphs; repeat the visual grammar without repeating the same composition.

Use shot duration and stillness to create suspense. Do not add motion merely to avoid a static frame.

## 3. Build production-ready assets

For collage, layered motion, or parallax:

1. List every semantic object needed for motion: background, structure, subject, foreground, cards, evidence, typography, atmosphere.
2. Prepare each as a complete independent asset with clean transparency and no fragments of neighboring objects.
3. Reconstruct the approved still from those source assets.
4. Inspect an asset contact sheet for clean alpha edges, scale, texture consistency, and correct occlusion.
5. Animate only after the reconstructed still matches the approved composition.

Never derive moving mirror frames, cards, cracks, hands, or foreground pieces from rough masks cut out of a flattened final composite. That leaks unrelated fragments during motion.

For generative video, use the same logic conceptually: isolate subject action, camera move, atmosphere, and transition instead of asking for every element to transform at once.

## 4. Use the motion grammar

Prefer:

- slow rostrum push or pull
- measured lateral track across a printed scene
- small parallax between paper planes
- rule-line wipe, shutter, page edge, ink spread, or registration slip
- controlled type impact followed by stillness
- subtle rain, fog, paper lift, lamp flicker, or wet reflection
- match cuts based on clocks, circles, windows, type blocks, or light

Avoid:

- glitch presets, whip zooms, spins, bounce, elastic UI motion
- constant handheld shake or artificial film damage
- every layer drifting independently
- dramatic 3D camera travel through a flat newspaper
- fast montage that erases hierarchy
- morphing architecture, changing faces, unstable type, and boiling texture

Keep camera direction explicit: start frame, end frame, focal subject, move speed, and what must remain geometrically stable.

## 5. Direct sound and subtitles

### Sound

Build a sparse acoustic world:

- rain on glass, distant rail, low city bed, paper, typewriter, clock, room tone
- restrained low strings, brushed percussion, muted brass, or no music
- one motivated accent for a reveal rather than a trailer-style impact on every cut

Avoid generic epic trailer music, cyber pulses, loud risers, constant vinyl crackle, and cartoon Foley.

### Bilingual subtitles

- Put concise Chinese above and original English below unless the project requires the reverse.
- Use semantic phrases, not raw speech-pause fragments.
- Merge short adjacent fragments when they form one thought.
- Keep the card calm and compact; do not cover faces, speaker labels, or key evidence.
- Prefer Source Han Serif/Songti for Chinese and an editorial serif or restrained humanist sans for English.
- Use charcoal/ivory with a restrained dark field or rule when needed; avoid oversized boxes and decorative distressed text.
- Preserve proper nouns, product names, API/SDK/CLI terms, and shortcuts in their original form unless asked to translate them.

## 6. Generate, composite, and inspect

For each shot:

1. Write the subject action and camera motion before style language.
2. Keep one primary motion and no more than two subtle environmental motions.
3. Name what must remain stable.
4. Generate a short test or animate the approved assets.
5. Inspect the first frame, final frame, and at least one middle frame.
6. Check identity, geometry, type, paper scale, ink behavior, palette, and temporal coherence.
7. Check the edit with sound and subtitles at delivery size.
8. Revise the failing shot or asset, not the entire sequence, when continuity is otherwise sound.

For a finished export, verify duration, resolution, frame rate, audio presence, subtitle legibility, and file playback.

## 7. Reusable sequence brief

```text
FORMAT
[DURATION], [ASPECT RATIO], [RESOLUTION/FRAME RATE if known], [DELIVERY CONTEXT].

EDITORIAL IDEA
[ONE-SENTENCE STORY OR ARGUMENT].

CONTINUITY
Interwar British private-press editorial; cool gray newsprint, charcoal ink,
restrained [BURGUNDY/GREEN/BRASS] accent; [PRINT PROCESS]; quiet film-noir light;
historically grounded London atmosphere; precise focal hierarchy.

SHOT 1 — HEADLINE — [TIME RANGE]
[SUBJECT/ACTION]. Camera: [START, END, SPEED]. Light: [MOTIVATED SOURCE].
Stable: [IDENTITY/GEOMETRY/TEXT]. Environmental motion: [ONE OR TWO ITEMS].

SHOT 2 — EVIDENCE OR TURN — [TIME RANGE]
[SUBJECT/ACTION]. Transition is motivated by [RULE/PAGE/OBJECT/LIGHT/SOUND].

SHOT 3 — IMPRINT — [TIME RANGE]
[FINAL IMAGE OR MARK]. Hold for [DURATION] so the idea lands.

TYPE AND SUBTITLES
[HEADLINE/CREDIT/SUBTITLE HIERARCHY, SAFE AREAS, LANGUAGE ORDER].

SOUND
[ROOM TONE], [MUSIC RESTRAINT], [ONE MOTIVATED ACCENT].

AVOID
Generic sepia, cyberpunk/neon, glossy 3D, steampunk clutter, propaganda geometry,
glitch/zoom/spin templates, unstable faces or architecture, morphing type,
uniform film damage, crushed shadows, overcrowded subtitles.
```
