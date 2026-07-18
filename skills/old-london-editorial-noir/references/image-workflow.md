# Still Image Workflow

## Contents

1. Choose the image language
2. Construct the prompt
3. Handle type
4. Adapt by artifact
5. Generate and inspect
6. Reusable prompt skeleton

## 1. Choose the image language

Select one dominant mode:

- **Printed photograph:** realistic subject and lighting translated through coarse newspaper halftone and ink gain.
- **Architectural engraving:** etched line, crosshatching, plate wear, and controlled paper field.
- **Commercial newspaper illustration:** bold silhouette, limited spot color, hand-drawn advertising energy.
- **Editorial paper collage:** independent cut-paper or printed fragments with strong hierarchy and real occlusion.
- **Printer’s mark:** simplified monochrome line ornament that survives at small scale.

Use a secondary mode only when the concept needs contrast. A printed photograph with an engraved border can work; a photograph, etching, collage, watercolor, and glossy 3D object in one frame usually cannot.

## 2. Construct the prompt

Write prompts in this order:

1. **Subject and action:** identify what must be recognizable before describing style.
2. **Scene and period:** state the place, architecture, weather, time, and historically relevant objects.
3. **Composition:** name the shot size, angle, focal hierarchy, crop, and negative-space reservation.
4. **Light:** state a motivated source such as gaslight, window light, overcast sky, or wet-street reflection.
5. **Print process:** choose specific halftone, letterpress, etching, screen-print, or collage behavior.
6. **Paper and palette:** name the stock, primary ink, and limited accent.
7. **Mood:** use quiet noir terms without obscuring the subject.
8. **Quality constraints:** require legible anatomy, architecture, silhouettes, or product shape.
9. **Negative prompt:** list the most plausible drift modes for the artifact.

Put the unique subject and composition before long style vocabulary. Do not let “vintage” replace factual scene direction.

## 3. Handle type

- Generate a clean image field with intentional space for copy.
- Add exact mastheads, titles, dates, captions, prices, credits, and body copy in a layout or compositing tool.
- If type must be generated in-image, limit it to a few large words and verify every character.
- Keep blackletter to the masthead or a very short identity role.
- For bilingual work, let one language lead and the other support; do not create two competing posters.

## 4. Adapt by artifact

### Portrait or scene

Prioritize the subject’s expression, gesture, and lighting. Apply print texture while preserving eyes, hands, and silhouette. Favor medium contrast with one deep-black anchor.

### Poster or cover

Reserve clear title space. Use one dominant image, one headline zone, and a small information band. Avoid filling the frame with fake micro-copy.

### Advertisement

Choose one period commercial voice and one product claim. Use strong display type, a product illustration, price or proof detail, and rules. Keep the advertised object recognizable.

### Logo or printer’s mark

Generate or draw in monochrome first. Use knot logic and natural negative space; introduce wheat or star only as subtle structure. Test at 24 px and in one ink.

### Editorial collage

Build complete semantic objects as independent pieces rather than cropping them from a final composite. Check alpha edges, shadows, paper thickness, and occlusion before arranging the frame.

### Existing image edit

Preserve identity, pose, geometry, and important copy unless the user requests changes. Localize the new print treatment to believable surfaces and tonal regions. Do not merely add a brown overlay and noise.

## 5. Generate and inspect

After each generation:

1. View the full image at intended size.
2. Check subject identity, anatomy, architecture, and important objects.
3. Check the first, second, and third visual reads.
4. Zoom in to confirm halftone, paper, ink edges, and local misregistration are intentional.
5. Check that the paper is not uniformly yellow and the shadows are not crushed.
6. Check for accidental modern tech, steampunk clutter, propaganda geometry, gibberish type, and decorative landmarks.
7. Revise the smallest failing layer of the prompt. Do not rewrite a successful composition just to fix texture.

## 6. Reusable prompt skeleton

```text
[SUBJECT AND ACTION], [SPECIFIC PLACE/PERIOD/WEATHER].
[SHOT, ANGLE, CROP, FOCAL HIERARCHY], with intentional negative space at [LOCATION]
for [TITLE/CAPTION if needed]. Motivated [LIGHT SOURCE], [SHADOW CHARACTER].

Rendered as [DOMINANT IMAGE LANGUAGE]: interwar British private-press editorial,
[SPECIFIC PRINT PROCESS], coarse visible halftone or engraved line where appropriate,
localized ink gain and slight plate misregistration, tactile [PAPER STOCK].
Charcoal-black primary ink with restrained [ACCENT] only.
Quiet film-noir atmosphere, historically grounded, precise and highly legible subject.

Avoid: generic sepia wash, neon, cyberpunk, futuristic UI, glossy 3D, plastic,
smooth vector finish, purple-blue tech palette, steampunk clutter, uniform grunge,
Soviet emblem geometry, propaganda poster, red-star-and-wheat motif,
illegible generated body text, crushed shadows, excessive blur.
```

Only keep terms relevant to the requested image. A shorter specific prompt is stronger than the full skeleton pasted mechanically.
