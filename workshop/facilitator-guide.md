# Facilitator guide

## Workshop purpose

This workshop gives beginners a complete, low-stakes path from an idea to a public website. It uses the same workflow they will use on future projects: work locally in VS Code, ask Copilot for bounded help, review a diff, commit with Git, push to GitHub, and deploy with GitHub Pages.

The starter site is intentionally framework-free. Learners can focus on the relationship between HTML structure, CSS presentation, JavaScript behavior, Git history, and the deployment workflow.

## Learning outcomes

Learners will be able to:

- describe how VS Code, Git, GitHub, Copilot, and GitHub Pages work together;
- create a repository with the special `username.github.io` name;
- edit semantic HTML, responsive CSS, and small JavaScript enhancements;
- write bounded Copilot prompts and inspect AI-generated changes;
- use a local preview and basic accessibility checks; and
- publish and update a static site through GitHub Actions.

## Suggested timing: 110 minutes

| Time | Activity | Facilitator move |
| --- | --- | --- |
| 0–10 min | Welcome and outcome | Show the finished site and explain the final URL. |
| 10–20 min | Tool map | Draw the path: VS Code → Git → GitHub → Pages. Explain Copilot as an assistant inside the editor. |
| 20–30 min | Education setup | Explain optional student verification and privacy. Do not make an individual’s account status public. |
| 30–40 min | Repository and clone | Demonstrate the `username.github.io` naming rule and open the repo in VS Code. |
| 40–60 min | Content pass | Learners replace sample copy, links, and projects. Pair them for a quick content check. |
| 60–75 min | Copilot loop | Model one prompt: ask for an accessibility audit, inspect the answer, make one change, and test it. |
| 75–90 min | Local testing | Test mobile layout, keyboard focus, links, and the menu. |
| 90–105 min | Commit and Pages | Push the site, select GitHub Actions as the Pages source, and watch the workflow. |
| 105–110 min | Share and exit ticket | Learners share their URL and answer the reflection questions below. |

If time is short, make the Education section a pre-work item and omit the optional challenge. If time is available, add a second iteration after partner feedback.

## Before the session

- Confirm that learners can access GitHub and VS Code, or prepare GitHub Codespaces as a fallback.
- Decide whether this repository will be marked as a GitHub template.
- Test the Pages workflow in a public repository before the session.
- Prepare a sample `username.github.io` site using fictional details.
- Decide how learners will share links without exposing information they want to keep private.
- Remind learners that public websites should contain only information they are comfortable publishing.

## Teaching notes

### Make the tool roles explicit

Use this simple vocabulary:

- **VS Code:** where we read and edit files.
- **Git:** the version history and local change tracker.
- **GitHub:** the remote home for the repository and collaboration history.
- **Copilot:** an AI assistant that proposes or explains code and copy.
- **GitHub Pages:** the hosting service that publishes the static files.

Learners often think “GitHub is the website.” Clarify that GitHub stores the source repository; Pages serves the published site from that repository.

### Model review, not magic

Before sending a prompt, say what context matters. After Copilot responds, ask:

1. What changed?
2. Which facts did it assume?
3. How can we test this?
4. What would make us reject the suggestion?

A strong live demo is the accessibility audit prompt in [`copilot-prompts.md`](copilot-prompts.md). It shows that Copilot can explain and review, not only generate.

### Keep personal data safe

GitHub Pages sites are public. Encourage a public email alias or contact form link instead of a personal phone number. Do not ask learners to paste private school records, API keys, passwords, or confidential work into Copilot.

### Support mixed experience levels

- Newer learners can change text, colors, and links first.
- Intermediate learners can add a project card or improve the mobile breakpoint.
- Advanced learners can add a theme toggle, custom domain, or a separate project page while keeping the site dependency-free.

Pair a learner who is comfortable with Git with someone who is new to the terminal, but let each person keep their own repository and make their own decisions.

## Assessment and exit ticket

Use the checklist in the participant guide as the completion assessment. For a quick exit ticket, ask learners to answer:

1. Which file controls something you can see on the page?
2. What did Copilot suggest, and how did you verify it?
3. What is your live URL?
4. What is the next change you want to make?

Evidence of learning is a working site plus a short explanation of one reviewed change, not the visual polish of the design.

## Common recovery paths

Keep [`troubleshooting.md`](troubleshooting.md) open during the deployment section. The most common problems are:

- repository name does not match the `username.github.io` pattern;
- workflow file was copied into the wrong folder;
- Pages source is still set to a branch instead of GitHub Actions;
- the first deployment is still running; or
- a file path uses uppercase letters locally but a different case in the HTML link.

If a learner cannot get Pages live during the session, have them show the local preview and the green commit. Deployment is a distinct troubleshooting skill, not a reason to invalidate the build.
