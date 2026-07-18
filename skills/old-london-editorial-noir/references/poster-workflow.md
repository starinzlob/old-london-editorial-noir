# Screen-Printed Poster Workflow

## Contents

1. Extract the requested reference layer
2. Choose one poster mode
3. Build the material stack
4. Control typography
5. Adapt themes safely
6. Inspect the result
7. Prompt skeletons

## 1. Extract the requested reference layer

Before prompting from a reference, classify what it contains:

- **Structure:** grid, crop, title scale, negative space, image-to-type relationship.
- **Material:** halftone size, screen mesh, ink coverage, paper, misregistration.
- **Motifs:** people, props, creatures, architecture, diagrams, symbols.
- **Era codes:** palette, coordinates, wireframes, crosshairs, calibration marks, scan-line graphics.
- **Copy:** title, slogan, labels, technical microtext.

Write one sentence stating which layers to inherit. If the user asks only for the print style, inherit material and optionally structure; replace motifs, era codes, palette, and copy.

Do not treat visible registration symbols as the same thing as physical misregistration. Prefer a slight color-edge shift in the ink itself. Add targets, crosses, coordinates, or printer marks only when explicitly requested.

## 2. Choose one poster mode

### Monumental type windows

Use for iconic themes, characters, creatures, places, or collectible campaign art.

- Fill roughly the upper 70–80 percent with one short, ultra-condensed outlined title.
- Let the scene appear through the letterforms.
- Let one recognizable silhouette cross the central letters instead of remaining trapped inside every glyph.
- Keep the lower 20–30 percent as one clean information band.
- Use only simple rules in the footer. Do not add decorative technical diagrams by default.
- Stack a long title into two lines rather than shrinking it.

Reading order: giant title, subject silhouette, subtitle band.

### Solid-headline editorial poster

Use for product claims, Skill promotion, railway adverts, tools, or concepts that need clearer conversion copy.

- Use one large solid condensed headline.
- Pair it with one dominant halftone image or a single diagonal/vertical image field.
- Add one burgundy side strip, wedge, or rule system—not several competing devices.
- Keep enough raw paper visible to prove the material.

Reading order: claim, image, product or credit line.

Do not mix monumental outline windows and a competing solid headline at equal scale.

## 3. Build the material stack

Use a physical two-to-four-ink print system:

- cool-gray or faded-ivory fibrous newsprint
- charcoal-black primary ink
- deep burgundy as the main spot color
- forest green as an optional quiet second accent
- brass only for tiny narrative details

Specify coarse visible halftone dots, screen mesh, dry ink, letterpress gain, local paper show-through, worn print edges, and slight plate shift. Keep defects local and uneven. Do not solve the texture with uniform grain, a sepia overlay, or digital scan lines.

## 4. Control typography

Generated poster copy should contain no more than four tiers:

1. a one-to-three-word title
2. one short campaign line
3. one location, category, or capability line
4. one tiny credit

Quote every line verbatim. Require no other text. Verify spelling at full size after generation.

Use real editable type instead when the copy is long, bilingual, legally important, or expected to change. For generated type-window posters, keep Chinese as a later editable overlay rather than forcing long Chinese copy into the bitmap.

## 5. Adapt themes safely

- Preserve a theme through silhouette, setting, gesture, and one signature prop.
- Avoid reproducing an actor's face or a film's official logo.
- For copyrighted characters, prefer original silhouettes or thematic reinterpretation unless the user explicitly needs licensed identity.
- If the image tool blocks a character after one targeted retry, stop renaming the same character. Offer a transparent thematic alternative, such as a web-and-rooftop motif instead of a masked superhero, and disclose the change.
- Do not let theme recognition override the Old London material system.

## 6. Inspect the result

Reject or revise when:

- the poster reads as a desk mockup, newspaper object, glossy key art, or generic sepia photograph
- the title is misspelled, too small, or competes with a second headline
- the subject disappears behind the letters or becomes unrecognizable at phone size
- the footer contains invented microtext or retro-technology ornaments
- misregistration appears as decorative crosshairs rather than displaced ink
- the reference's objects or era symbols survive after the user asked only for its print texture
- halftone looks like uniform digital noise instead of ink dots on paper

## 7. Prompt skeletons

### Monumental type windows

```text
[THEME AND RECOGNIZABLE SUBJECT], [PERIOD PLACE AND ATMOSPHERE].
Create a vertical campaign poster with the enormous ultra-condensed outlined title
"[SHORT TITLE]" filling the upper three-quarters as image windows.
[SUBJECT] crosses the central letterforms. Keep the lower band typographic only.

Text, verbatim: "[TITLE]"; "[CAMPAIGN LINE]"; "[CONTEXT LINE]"; "[CREDIT]".
No other text.

Physical three-color screen print on cool-gray fibrous newsprint:
charcoal ink, deep burgundy, restrained forest green, coarse visible halftone,
dry ink, local dropout, letterpress gain, slight color-edge misregistration.

Exclude wireframe globes, coordinates, crosshairs, calibration targets,
technical diagrams, scan-line ornaments, vaporwave grids, glossy 3D,
actor likenesses, official logos, fake words, and extra microtext.
```

### Solid-headline editorial poster

```text
[SUBJECT OR CONCEPT] as an original vertical British editorial screen-print poster.
Use one large solid condensed headline "[CLAIM]", one dominant halftone image field,
one burgundy structural accent, and generous raw-paper negative space.

Text, verbatim: "[CLAIM]"; "[PRODUCT OR STYLE NAME]"; "[CAPABILITY LINE]".
No other text.

Use cool-gray newsprint, charcoal ink, deep burgundy, coarse halftone,
screen mesh, dry ink, paper fibers, local dropout, and slight plate shift.
Avoid outline-window lettering, retro-tech ornaments, glossy key art,
uniform grunge, fake copy, and unrelated reference motifs.
```
