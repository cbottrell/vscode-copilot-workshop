# Build and publish your Forrest Research Foundation profile with VS Code, GitHub, and Copilot

This repository is a ready-to-run PhD Surgery workshop for Forrest Research Foundation Scholars (PhD students) and Fellows (postdocs) who want to create a public research profile and publish it with GitHub Pages. The project uses plain HTML, CSS, and JavaScript so participants can inspect every line, ask Copilot for help, and understand the result before they commit it.

## Workshop at a glance

- **Audience:** Forrest Research Foundation Scholars and Fellows, including beginner web developers
- **Duration:** 90–120 minutes
- **Outcome:** a live research profile at `https://YOUR-USERNAME.github.io`
- **Platforms:** Windows, macOS, Linux, or GitHub Codespaces
- **Tools:** GitHub, VS Code, Git, and GitHub Copilot
- **Format:** short demos, guided build, pair review, and an individual extension challenge

The workflow is platform-neutral. Participants can use the VS Code integrated terminal with PowerShell, Git Bash, macOS/Linux shells, or GitHub Codespaces. The participant guide includes the small command differences.

## What is included

| Path | Purpose |
| --- | --- |
| [`index.html`](index.html) | Semantic starter page with editable content | 
| [`styles.css`](styles.css) | Responsive visual design with no framework dependency |
| [`script.js`](script.js) | Small progressive-enhancement script for the menu and year |
| [`.github/workflows/pages.yml`](.github/workflows/pages.yml) | GitHub Pages deployment workflow |
| [`.github/copilot-instructions.md`](.github/copilot-instructions.md) | Project rules that keep Copilot’s suggestions focused |
| [`workshop/participant-guide.md`](workshop/participant-guide.md) | Learner-facing, step-by-step lab |
| [`workshop/facilitator-guide.md`](workshop/facilitator-guide.md) | Timing, setup, teaching notes, and troubleshooting |
| [`workshop/copilot-prompts.md`](workshop/copilot-prompts.md) | Copy-ready prompt cards for the build |
| [`workshop/troubleshooting.md`](workshop/troubleshooting.md) | Recovery paths for common GitHub Pages issues |

## Participant template

Use the separate [Forrest Research Foundation profile template](https://github.com/cbottrell/forrest-research-profile-template) for participant repositories. It contains only the starter website, Pages workflow, Copilot instructions, and a short setup README. This repository remains the facilitator source with the full workshop guides and prompt cards.

## How to run the workshop

1. Share this repository for the workshop instructions and the [participant template](https://github.com/cbottrell/forrest-research-profile-template) for starter files.
2. Ask each participant to choose **Use this template → Create a new repository**.
3. Have participants name the new **public** repository `YOUR-USERNAME.github.io`, then open it in VS Code.
4. Follow [`workshop/participant-guide.md`](workshop/participant-guide.md) from top to bottom.
5. Use the facilitator guide to pause for the suggested research-profile checkpoints and pair reviews.

Forrest Research Foundation affiliation and GitHub Education verification are separate. Participants do not need GitHub Education verification to complete the project. Verified students can optionally apply for the GitHub Student Developer Pack and activate Copilot Student; the participant guide explains that path without making it a blocker.

## Success criteria

By the end, each participant should be able to:

- explain the role of VS Code, Git, GitHub, Copilot, and GitHub Pages;
- use Copilot to propose and explain small changes instead of blindly accepting a full rewrite;
- introduce themselves as a Forrest Research Foundation Scholar or Fellow working at Curtin, Murdoch, UWA, ECU, or Notre Dame;
- make a semantic, responsive research profile with accessible links and public-safe research descriptions;
- commit and push a change to GitHub; and
- find the live site and diagnose a failed Pages deployment.

## Official links

- [GitHub Education for students](https://education.github.com/pack/join)
- [Access GitHub Copilot for free as a student](https://docs.github.com/en/copilot/how-tos/copilot-on-github/set-up-copilot/enable-copilot/set-up-for-students)
- [Create a GitHub Pages site](https://docs.github.com/en/pages/getting-started-with-github-pages/creating-a-github-pages-site)
- [Use custom workflows with GitHub Pages](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages)

## License and adaptation

Use this workshop as a teaching resource for your PhD Surgery session. Replace the sample copy with the participant’s name, Scholar/Fellow status, university, research area, and public links. Keep the privacy and research-integrity guidance: GitHub Pages sites are public by default, so participants should publish only information they are comfortable sharing and only research details that are safe to make public.
