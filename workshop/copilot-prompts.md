# Copilot prompt cards

Use these prompts in small iterations. Replace the bracketed text before sending a prompt. If Copilot proposes a large rewrite, ask it to explain the plan first and apply one part at a time.

## Content, affiliation, and voice

```text
Act as an editor. Based on this true information about me: I am a Forrest Research Foundation [Scholar / Fellow] working at [Curtin / Murdoch / UWA / ECU / Notre Dame] and researching [YOUR FIELD]. Suggest five hero taglines under 12 words. Keep the tone [THREE ADJECTIVES]. Do not add achievements, affiliations, funding, or research claims I did not mention. Return options only.
```

```text
Rewrite the paragraph in index.html to sound like a thoughtful research profile for a Forrest Research Foundation Scholar or Fellow. Keep the facts and affiliation unchanged, use plain language, and keep it under 55 words. Do not reveal or invent unpublished research. Show the proposed replacement before editing.

```text
Audit the Forrest Research Foundation affiliation and university statement in index.html. Check that it clearly distinguishes Scholar from Fellow, uses one of Curtin, Murdoch, UWA, ECU, or Notre Dame, and leaves unknown details as placeholders. Do not edit the file.
```
```

## Structure and HTML

```text
Explain the semantic structure of index.html section by section. Identify the main heading, navigation landmark, content sections, and link purposes. Do not edit the file.
```

```text
Add one research card to index.html using the same structure as the existing cards. Use these public facts only: [PROJECT OR OUTPUT], [PUBLIC DESCRIPTION], [YOUR ROLE], [LINK]. Do not add unpublished findings, participant details, or claims about impact. Keep the heading order and write descriptive link text.

```text
Review this research-profile copy for publication safety. Flag anything that sounds like unpublished findings, identifiable participant information, confidential supervision or review material, embargoed results, or an unsupported claim. Return suggested safer wording, but do not edit until I approve it.
```
```

## Responsive design

```text
Inspect styles.css and describe how the layout behaves at 1200px, 760px, and 360px. List any content that may overflow or become hard to read. Do not edit yet.
```

```text
Make the project cards readable at 360px wide. Preserve the color palette and desktop layout, use the existing breakpoint when possible, and explain each changed selector after the patch.
```

## Accessibility

```text
Audit index.html and styles.css for: one clear h1, logical heading order, keyboard focus, link purpose, color contrast, readable line length, reduced motion, and mobile navigation labels. Return findings by priority with file names. Do not make changes.
```

```text
Suggest an accessible label for every icon-only or symbol-only element in this page. Prefer visible text when it improves clarity. Do not add ARIA where native HTML already solves the problem.
```

## Debugging

```text
The mobile menu does not open. Trace the interaction across index.html, styles.css, and script.js. Explain the likely cause, show the smallest safe fix, and give me one browser test to confirm it.
```

```text
My GitHub Pages workflow completed, but the page is blank. Give me a diagnostic checklist that checks the deployed artifact, file names, relative paths, and the browser console. Do not assume the cause.
```

## Reflection

```text
Ask me three questions that would help me decide whether this research output belongs on a public profile. Ask about audience, publication safety, and whether the claim is accurate. Wait for my answers before suggesting copy.
```

```text
Explain this CSS rule as if I have written basic CSS but do not yet understand [PROPERTY OR VALUE]. Use a tiny example and then connect it back to this page. Do not rewrite the stylesheet.
```

## Prompt hygiene

- Tell Copilot what is true and what is still a placeholder.
- Ask for a plan or explanation before a large edit.
- Avoid pasting private data, passwords, API keys, unpublished research, participant information, embargoed results, or confidential assignment/supervision material.
- Read the diff, run the page, and test the changed behavior.
- Treat generated copy as a draft: check tone, accuracy, and originality.
