---
name: old-london-editorial-noir
description: Apply the Old London Editorial Noir visual system to image and video generation or editing. Use for illustrations, photographs, screen-printed campaign posters, monumental type-window layouts, covers, advertisements, logos, storyboards, title cards, motion graphics, social videos, cinematic sequences, and bilingual subtitled videos when the user asks for this named style, a signature/core/personal style, an old British newspaper look, interwar London, editorial film noir, halftone newsprint, letterpress, engraving, fog, rain, or gaslight. Also use to restyle or audit visual prompts and generated media against this system. Preserve an existing product design system when present, and do not apply the style when the user explicitly requests another direction.
---

# Old London Editorial Noir

Create images and videos that feel like a preserved private London newspaper brought to life: historically grounded, editorially precise, quietly cinematic, tactile, and readable.

## Load the right references

1. Read [references/canon.md](references/canon.md) completely before making visual decisions.
2. For a still image, image edit, poster, cover, logo, or keyframe, also read [references/image-workflow.md](references/image-workflow.md).
3. For a campaign poster, social launch graphic, screen-printed advert, or typography-led cover, also read [references/poster-workflow.md](references/poster-workflow.md).
4. For animation, motion graphics, title sequences, or finished video, also read [references/video-workflow.md](references/video-workflow.md).
5. For mixed work, establish the still-image system first, then translate it into motion.

## Build the style contract

Before generation, reduce the request to a compact internal contract:

- **Story:** the subject, action, place, period, and emotional beat.
- **Editorial role:** lead image, portrait, advertisement, archive plate, diagram, logo, title card, video scene, or full sequence.
- **Hierarchy:** the first focal point, second read, and deliberate negative space.
- **Material:** newsprint, letterpress, halftone, engraving, screen print, or a restrained mixture with a reason.
- **Palette:** paper, primary ink, and no more than two limited accents.
- **Light:** the motivated source and the shape of shadow, fog, or rain.
- **Type:** real editable type whenever exact copy matters; period display faces only in short roles.
- **Drift guards:** name the most likely ways this specific piece could become generic retro, steampunk, propaganda, or modern tech.

Do not turn the contract into visible process unless the user asks. Use it to keep every frame, asset, and revision coherent.

## Execute

1. Preserve the subject and communication goal before adding atmosphere.
2. When a reference is supplied, separate its composition, print process, subject motifs, palette, and era codes. Inherit only the layers the user requested.
3. Choose one dominant image-making language. Do not mix newspaper photo, etching, collage, and glossy cinema without a narrative reason.
4. Put historical texture in the image-making process: visible halftone, ink gain, local misregistration, paper fibers, or engraved hatching. Avoid a uniform noise overlay.
5. Keep the subject legible. Mystery must come from framing, occlusion, light, and pacing—not from crushing all detail.
6. Use charcoal and cool newsprint as the default base. Add burgundy, forest green, brass, cream, or deep brown sparingly.
7. Keep exact titles, captions, credits, subtitles, and UI copy as real text when the production tool allows it. Do not trust image generation for critical spelling.
8. Generate or edit the requested artifact with the available image or video tool. Match the tool to the task; this Skill defines art direction rather than requiring one vendor.
9. Inspect the actual output, not just the prompt. Revise the prompt, source assets, timing, crop, or typography until it passes the acceptance gate.

## Acceptance gate

Reject or revise the result if any answer is no:

- Does it read specifically as British private press or interwar London rather than generic sepia “vintage”?
- Is there one clear focal point and a deliberate reading order?
- Are paper and ink materially present without damaging clarity?
- Is the palette restrained and free of accidental purple-blue tech color?
- Are historical cues selective instead of a pile of gears, pipes, stamps, and props?
- Is all necessary text readable, correctly spelled, and placed with editorial discipline?
- If a reference supplied only print or layout direction, did the result avoid copying its objects, slogans, palette, and era-specific ornaments?
- For a social poster, are the title, subject silhouette, and information band legible at phone size?
- Does the result avoid Soviet-emblem, propaganda-poster, steampunk, cyberpunk, glossy 3D, and modern SaaS associations?
- For video, do motion, transitions, subtitles, and sound belong to the same quiet editorial world as the still frames?

Run `python3 scripts/check_style_brief.py <brief-or-prompt-file> --target image|video` when a written prompt or creative brief needs a fast preflight. Treat warnings as review cues, not substitutes for visual judgment.

## Respect overrides

- Follow an explicit user direction that conflicts with this canon.
- For an established brand or product, preserve its conventions and blend this system only where appropriate.
- Do not force London landmarks, period props, or distressed paper into work that only needs the underlying hierarchy, restraint, and tactile print logic.
