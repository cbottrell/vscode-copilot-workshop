# Copilot prompt cards

Use these prompts in small iterations. Replace the bracketed text before sending a prompt. If Copilot proposes a large rewrite, ask it to explain the plan first and apply one part at a time.

## Content and voice

```text
Act as an editor. Based on this true information about me: [PASTE 2–3 FACTS], suggest five hero taglines under 12 words. Keep the tone [THREE ADJECTIVES]. Do not add achievements, employers, or technologies I did not mention. Return options only.
```

```text
Rewrite the paragraph in index.html to sound more like a thoughtful student portfolio. Keep the facts unchanged, use plain language, and keep it under 55 words. Show the proposed replacement before editing.
```

## Structure and HTML

```text
Explain the semantic structure of index.html section by section. Identify the main heading, navigation landmark, content sections, and link purposes. Do not edit the file.
```

```text
Add one project card to index.html using the same structure as the existing cards. Use these facts only: [PROJECT NAME], [WHAT IT DOES], [YOUR ROLE], [LINK]. Keep the heading order and write descriptive link text.
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
Ask me three questions that would help me decide whether this project belongs in my portfolio. Wait for my answers before suggesting copy.
```

```text
Explain this CSS rule as if I have written basic CSS but do not yet understand [PROPERTY OR VALUE]. Use a tiny example and then connect it back to this page. Do not rewrite the stylesheet.
```

## Prompt hygiene

- Tell Copilot what is true and what is still a placeholder.
- Ask for a plan or explanation before a large edit.
- Avoid pasting private data, passwords, API keys, or confidential assignment material.
- Read the diff, run the page, and test the changed behavior.
- Treat generated copy as a draft: check tone, accuracy, and originality.
