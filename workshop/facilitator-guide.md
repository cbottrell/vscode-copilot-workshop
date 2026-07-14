# Facilitator guide

## Workshop purpose

This PhD Surgery workshop gives Forrest Research Foundation Scholars (PhD students) and Fellows (postdocs) a complete, low-stakes path from a research profile idea to a public website. It uses the same workflow they will use on future projects: work locally in VS Code, ask Copilot for bounded help, review a diff, commit with Git, push to GitHub, and deploy with GitHub Pages.

The starter site is intentionally framework-free. Participants can focus on the relationship between HTML structure, CSS presentation, JavaScript behavior, Git history, and the deployment workflow while translating research for a public audience.

## Learning outcomes

Participants will be able to:

- describe how VS Code, Git, GitHub, Copilot, and GitHub Pages work together;
- create a repository with the special `username.github.io` name;
- edit semantic HTML, responsive CSS, and small JavaScript enhancements;
- write an accurate Forrest Research Foundation Scholar/Fellow and university affiliation statement;
- describe research in a public-safe way without exposing unpublished or confidential material;
- write bounded Copilot prompts and inspect AI-generated changes;
- use a local preview and basic accessibility checks; and
- publish and update a static site through GitHub Actions.

## Platform support

This workshop is designed for Windows, macOS, Linux, and GitHub Codespaces. Keep the workflow consistent across the room:

- Use the VS Code integrated terminal so the editor, files, and Git history are visible together.
- On Windows, demonstrate PowerShell for the local server (`py -m http.server 8000`) and mention that Git Bash can use the macOS/Linux command (`python3 -m http.server 8000`).
- On macOS and Linux, use `python3 -m http.server 8000`.
- If a participant does not have Python, use VS Code Live Preview or GitHub Codespaces rather than spending the workshop installing a runtime.
- If `code .` is unavailable, demonstrate **File → Open Folder** in VS Code.
- Keep file paths and URLs in examples platform-neutral by using `/` in repository paths and links.
- The repository’s `.gitattributes` file normalises text line endings so Windows and Unix-based systems do not create noisy diffs.

## Suggested timing: 110 minutes

| Time | Activity | Facilitator move |
| --- | --- | --- |
| 0–10 min | Welcome and outcome | Show the finished site and explain the final URL. Introduce the profile as a public-facing research identity. |
| 10–20 min | Tool map | Draw the path: VS Code → Git → GitHub → Pages. Explain Copilot as an assistant inside the editor. |
| 20–30 min | Research profile brief | Explain the Scholar/Fellow distinction, the five university options, and the difference between public research summaries and unpublished work. |
| 30–40 min | Repository and clone | Demonstrate the `username.github.io` naming rule and open the repo in VS Code. |
| 40–60 min | Content pass | Participants replace sample copy, affiliation, research area, links, and public outputs. Pair them for a quick content check. |
| 60–75 min | Copilot loop | Model one prompt: ask for an accessibility audit, inspect the answer, make one change, and test it. |
| 75–90 min | Local testing | Test mobile layout, keyboard focus, links, and the menu. |
| 90–105 min | Commit and Pages | Push the site, select GitHub Actions as the Pages source, and watch the workflow. |
| 105–110 min | Share and exit ticket | Learners share their URL and answer the reflection questions below. |

If time is short, make GitHub Education verification a pre-work item and omit the optional challenge. If time is available, add a second iteration after partner feedback.

## Before the session

- Confirm that participants can access GitHub and VS Code on Windows, macOS, or Linux, or prepare GitHub Codespaces as a fallback.
- Share the [Forrest Research Foundation profile template](https://github.com/cbottrell/forrest-research-profile-template) and keep this repository as the workshop-instructions repository.
- Confirm the participant template is marked as a GitHub template and test **Use this template → Create a new repository** before the session.
- Ask participants to open the VS Code integrated terminal and check whether they are using PowerShell, Git Bash, or a macOS/Linux shell.
- Test the Pages workflow in a public repository before the session.
- Prepare a sample `username.github.io` site using fictional Scholar/Fellow, university, and research details.
- Decide how participants will share links without exposing information they want to keep private.
- Remind participants that public websites should contain only information they are comfortable publishing and only research details that are safe to make public.

## Teaching notes

### Make the tool roles explicit

Use this simple vocabulary:

- **VS Code:** where we read and edit files.
- **Git:** the version history and local change tracker.
- **GitHub:** the remote home for the repository and collaboration history.
- **Copilot:** an AI assistant that proposes or explains code and copy.
- **GitHub Pages:** the hosting service that publishes the static files.
- **Forrest Research Foundation Scholar/Fellow:** the public affiliation participants may use to introduce their research profile.

Learners often think “GitHub is the website.” Clarify that GitHub stores the source repository; Pages serves the published site from that repository.

### Model review, not magic

Before sending a prompt, say what context matters. After Copilot responds, ask:

1. What changed?
2. Which facts did it assume?
3. How can we test this?
4. What would make us reject the suggestion?

A strong live demo is the accessibility audit prompt in [`copilot-prompts.md`](copilot-prompts.md). It shows that Copilot can explain and review, not only generate.

### Keep personal data safe

GitHub Pages sites are public. Encourage a public email alias or contact form link instead of a personal phone number. Do not ask participants to paste unpublished thesis chapters, participant data, identifiable case studies, API keys, passwords, embargoed results, or confidential supervision/review material into Copilot.

### Support mixed experience levels

- Newer participants can change the affiliation statement, research summary, colors, and links first.
- Intermediate participants can add a public research output card or improve the mobile breakpoint.
- Advanced participants can add an ORCID link, DOI/publication list, theme toggle, custom domain, or separate project page while keeping the site dependency-free.

Pair a participant who is comfortable with Git with someone who is new to the terminal, but let each person keep their own repository and make their own decisions.

## Assessment and exit ticket

Use the checklist in the participant guide as the completion assessment. For a quick exit ticket, ask participants to answer:

1. Which file controls something you can see on the page?
2. How did you state your Forrest Research Foundation status and university?
3. What research detail did you choose to keep public-safe?
4. What did Copilot suggest, and how did you verify it?
5. What is your live URL and next change?

Evidence of learning is a working site plus a short explanation of one reviewed change and one public-safety decision, not the visual polish of the design.

## Common recovery paths

Keep [`troubleshooting.md`](troubleshooting.md) open during the deployment section. The most common problems are:

- repository name does not match the `username.github.io` pattern;
- workflow file was copied into the wrong folder;
- Pages source is still set to a branch instead of GitHub Actions;
- the first deployment is still running; or
- a file path uses uppercase letters locally but a different case in the HTML link.

If a participant cannot get Pages live during the session, have them show the local preview and the green commit. Deployment is a distinct troubleshooting skill, not a reason to invalidate the profile build.
