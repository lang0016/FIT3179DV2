# Activate GitHub Pages

The complete static website is on the repository's `main` branch. It is tested
locally, but **GitHub Pages has not been enabled**. The current expected site
address returns HTTP 404.

The repository integration allowed pushing the files, but GitHub rejected the
Pages-creation API request with **HTTP 403: Resource not accessible by integration**.
This is a GitHub integration permission limitation, not a website build error.
GitHub's official `actions/configure-pages@v5` input documentation states that
first-time enablement needs a different token with the appropriate permissions;
the workflow's default `GITHUB_TOKEN` cannot substitute for those permissions.
No token needs to be shared in chat.

## One-time account action

1. Open https://github.com/lang0016/FIT3179DV2/settings/pages while signed in.
2. Under **Build and deployment**, set **Source → Deploy from a branch**.
3. Select **main**, select **/(root)**, and click **Save**.
4. Wait for the Pages deployment to finish. The site address should be:
   https://lang0016.github.io/FIT3179DV2/
5. Open that URL in a private browser window. Confirm all twelve charts load,
   hover tooltips work and data tables open. Do not submit a URL that still
   returns 404 or asks visitors to sign in.

No additional build command, domain, API key or CDN configuration is needed.
The root `index.html`, `.nojekyll`, vendored libraries, chart specifications and
source data are already present. Future pushes to `main` will update the site
through the selected branch deployment.

## Optional automated public check

After the URL works, run from the repository root:

```sh
SITE_URL=https://lang0016.github.io/FIT3179DV2/ npm test
```

This uses a fresh anonymous browser context. It checks twelve chart renders,
requests, accessibility labels, layout, text collisions, paragraph line lengths,
sector highlighting and the data budget at four laptop widths.

The independent **Validate visualisation** GitHub Actions workflow tests the site
on a local HTTP server. A green validation workflow does not, by itself, mean
that Pages is enabled or the public site is live.
