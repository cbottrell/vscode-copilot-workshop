# Participant guide: ship your personal site

Welcome! In this workshop you will make a small portfolio site, use GitHub Copilot as a pair programmer, and publish the result with GitHub Pages.

The goal is not to produce the same design as everyone else. The goal is to leave with a real, public website that sounds like you and that you can keep improving.

## What you will finish

By the end of the lab, you will have:

- a GitHub repository named `YOUR-USERNAME.github.io`;
- a responsive personal site with an about section, projects, and contact links;
- at least one change suggested or explained by Copilot and reviewed by you;
- a commit pushed from VS Code to GitHub; and
- a live GitHub Pages URL.

## Before you start

You need:

- a GitHub account;
- VS Code installed and signed in to GitHub;
- Git installed, or access to a GitHub Codespace;
- GitHub Copilot in VS Code, if your facilitator has provided access; and
- three pieces of content: a short introduction, one or two projects, and links you are comfortable publishing.

### Optional: verify GitHub Education

If you are a student aged 13 or older, you can apply for the [GitHub Student Developer Pack](https://education.github.com/pack/join). GitHub may ask for a school email address or proof of enrollment. Once GitHub verifies your student status, follow [GitHub’s student Copilot instructions](https://docs.github.com/en/copilot/how-tos/copilot-on-github/set-up-copilot/enable-copilot/set-up-for-students) to activate Copilot Student.

This is optional for the workshop. If verification is pending, keep building with the access you already have. Offers and eligibility can change, so use the current GitHub pages linked above rather than relying on screenshots.

## 1. Plan your page before asking for code

Write quick answers to these prompts. They become your content brief:

1. What do you do or study?
2. What kind of work do you want to be known for?
3. Which two projects, assignments, or experiments can you show?
4. What is the safest public way for someone to contact you?
5. Which three words describe the mood of your site?

Do not publish your home address, personal phone number, private class information, passwords, API keys, or anything you would not put on a public noticeboard.

## 2. Create your personal website repository

On GitHub, create a **public** repository with this exact name:

```text
YOUR-USERNAME.github.io
```

Replace `YOUR-USERNAME` with your GitHub username. For example, if your username is `sam-lee`, the repository must be `sam-lee.github.io`.

If the facilitator has enabled this workshop repository as a template, choose **Use this template** and create your new repository from it. Otherwise, copy these starter files into your new repository:

```text
index.html
styles.css
script.js
.github/copilot-instructions.md
.github/workflows/pages.yml
```

## 3. Open the project in VS Code

Clone your repository from the repository page, then open it in VS Code. The integrated terminal commands look like this:

```bash
git clone https://github.com/YOUR-USERNAME/YOUR-USERNAME.github.io.git
cd YOUR-USERNAME.github.io
code .
```

If you are using GitHub Codespaces, open the repository in a codespace and skip the clone command.

You should see `index.html`, `styles.css`, `script.js`, and a `.github` folder in the Explorer. Open `index.html` in the editor and locate the sample name, biography, project cards, email address, and social links.

## 4. Make the starter site yours

Begin with a change you understand. Replace:

- `Alex Morgan` with your name;
- the hero sentence with a true one-line description of your work;
- the about paragraphs with your own words;
- the three sample projects with real work, class exercises, or experiments; and
- the sample links and email address with your public links.

Keep the HTML structure while you edit the content. This lets you see the difference between content, presentation, and behavior:

| File | Question to ask |
| --- | --- |
| `index.html` | What content and structure should a visitor see? |
| `styles.css` | How should that content look at different widths? |
| `script.js` | What small interaction or enhancement is useful? |

## 5. Use Copilot as a pair programmer

The workshop loop is:

> Ask → inspect → run → test → commit

Give Copilot context, constraints, and a clear definition of done. Start with one small request, then inspect the diff. You are responsible for the facts and the final code.

Try one of these prompts in Copilot Chat:

```text
Review index.html and suggest three concise hero taglines for a student who is studying [YOUR SUBJECT]. Do not invent achievements. Return options only; do not edit the file.
```

```text
In index.html, replace the three sample project cards with placeholders for my projects. Keep the existing semantic structure and link style. Do not invent project outcomes or technologies; use [REPLACE THIS] where information is missing.
```

```text
Review styles.css for mobile usability. Identify the two highest-impact issues at widths below 760px, explain why they matter, and propose a small patch. Do not change the desktop layout.
```

```text
Review this page for keyboard navigation, heading order, color contrast, link purpose, and reduced-motion support. Return a checklist with the relevant file and line area for each finding. Do not edit yet.
```

For more prompt cards, see [`copilot-prompts.md`](copilot-prompts.md).

## 6. Preview locally

Use the VS Code integrated terminal to start a tiny local server:

```bash
python3 -m http.server 8000
```

Open [http://localhost:8000](http://localhost:8000) in a browser. If `python3` is unavailable, use VS Code’s Live Preview extension or the equivalent local preview available in your environment.

Check the page at a wide and narrow width. In particular, verify:

- the menu opens and closes on a small screen;
- every link has a useful destination or is clearly a placeholder;
- focus is visible when you use the Tab key;
- text is readable without zooming out; and
- your content is accurate and does not expose private information.

Stop the server with `Ctrl+C` when you are finished previewing.

## 7. Commit and push from VS Code

Review the Source Control panel. You should recognize every changed file. Then run:

```bash
git add .
git commit -m "Create personal portfolio site"
git push -u origin main
```

If your repository uses `master` instead of `main`, push that branch instead. You can also stage, commit, and sync from the VS Code Source Control view.

## 8. Turn on GitHub Pages

The starter repository already contains `.github/workflows/pages.yml`. On GitHub:

1. Open your repository and choose **Settings**.
2. In the sidebar, choose **Pages**.
3. Under **Build and deployment**, set **Source** to **GitHub Actions**.
4. Open the **Actions** tab and watch the deployment workflow.
5. When it succeeds, return to **Settings → Pages** and choose **Visit site**.

Your personal site should be available at:

```text
https://YOUR-USERNAME.github.io
```

The first deployment can take a few minutes. A later push to `main` will run the workflow again and update the site.

## 9. Pair review and final polish

Swap links with a partner. Ask them to answer:

1. What do you think this person does after reading the first screen?
2. Which project would you click first, and why?
3. Can you find the contact method without being told where it is?
4. What is one detail that makes the site feel personal?

Use the feedback to make one small, meaningful change. Ask Copilot to explain the change if you are unsure why it works. Preview, commit, push, and check the live URL again.

## Optional challenge

Choose one extension:

- add a downloadable résumé link with a descriptive label;
- add a new project card and a project-specific page;
- create a light/dark theme toggle that respects the user’s system preference;
- add a small “now” section that you will update monthly; or
- write a short `README.md` in your personal repository explaining how you built the site.

Keep the site static and dependency-free unless you can explain why a new dependency is worth the maintenance cost.

## Done checklist

- [ ] My repository is named `YOUR-USERNAME.github.io`.
- [ ] My name, introduction, projects, and links are accurate.
- [ ] I checked the page on a narrow screen.
- [ ] I tested keyboard focus and the mobile menu.
- [ ] I reviewed Copilot’s changes before accepting them.
- [ ] I committed and pushed from VS Code.
- [ ] The GitHub Pages workflow is green.
- [ ] I can share my live URL safely.
