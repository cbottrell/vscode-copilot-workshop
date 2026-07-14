# GitHub Pages troubleshooting for the PhD Surgery profile workshop

Use this guide after checking the local site. Fix one layer at a time: content, local preview, Git history, workflow, then Pages settings.

## The local page is blank or shows the wrong content

1. Confirm that the file is named exactly `index.html`.
2. Open the browser developer tools and check the Console for errors.
3. Check that `styles.css` and `script.js` are linked with the correct lowercase names.
4. Refresh after saving the file.
5. If the local server is running from the wrong folder, stop it and run `python3 -m http.server 8000` from the repository root.

## The mobile menu does not open

Check that:

- the button has `aria-controls="site-nav"`;
- the navigation has `id="site-nav"`;
- `script.js` is loaded with `defer`; and
- the browser Console has no JavaScript errors.

Use Copilot to trace the interaction across all three files, then test with a narrow viewport and the keyboard.

## The GitHub Actions workflow is missing

The file must be at:

```text
.github/workflows/pages.yml
```

The leading dot in `.github` matters. Check the Source Control panel to confirm the workflow was included in the commit and pushed to the default branch.

## The workflow fails

Open the failed run in the repository’s **Actions** tab and read the first failed step. For this static site, check:

- the workflow file is valid YAML;
- `actions/checkout`, `actions/configure-pages`, `actions/upload-pages-artifact`, and `actions/deploy-pages` are spelled correctly;
- the workflow is running on the branch named in its `on.push.branches` list; and
- the repository has Pages enabled and the workflow has the required `pages: write` and `id-token: write` permissions.

Do not keep retrying without reading the log. Copy only the relevant error message into Copilot and ask it to explain the likely cause.

## The workflow is green but the site is not available

1. Open **Settings → Pages** and confirm the source is **GitHub Actions**.
2. Check the workflow run’s deployment job and environment.
3. Confirm the repository name is exactly `YOUR-USERNAME.github.io` if you expect a user site.
4. Wait a few minutes after the first successful deployment.
5. Open the site URL from the Pages settings instead of typing it manually.

## The site loads but CSS or links are broken

GitHub Pages URLs are case-sensitive. Use relative paths such as `styles.css`, not a local file path. For a user site, a link like `/about.html` may work differently than it does in a nested project site; prefer `about.html` for simple static files.

## A participant is blocked by Git authentication

Use the VS Code Source Control sign-in flow, GitHub CLI if it is already installed, or GitHub Codespaces. Do not ask a participant to share a password or personal access token in chat. If the group is using a managed machine, ask the facilitator or administrator to help with the approved sign-in method.

## GitHub Education verification is pending

GitHub Education verification is not required to finish this Forrest Research Foundation workshop. Continue with the GitHub account and tools already available. Return to the official [GitHub Education student page](https://education.github.com/pack/join) later. Forrest Research Foundation Scholar/Fellow status is separate from GitHub Education verification.
