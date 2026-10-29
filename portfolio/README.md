# Archit Khandelwal portfolio

Static HTML, CSS and JavaScript. No build or paid service is required.

## Live URL

Deployment pending GitHub Pages activation and Claude's review/merge. Expected URL after the workflow on `main` succeeds: https://architkhandelwal2005.github.io/freelance-ops/

## Publish

1. In repository **Settings → Pages**, set **Build and deployment → Source** to **GitHub Actions**.
2. Claude reviews this branch; Archit merges it into `main`. `.github/workflows/pages.yml` assembles `portfolio/` and `demos/` into one published site.
3. Open the URL above and verify the deployment. The workflow also displays the exact URL in its deployment environment.

## Update a case study

Edit the matching `<article class="work-card">` in `index.html`. Keep the client name and results factual; avoid confidential details. The fictional GEO audit is in `geo-sample.html`; its source example is in `deliverables/samples/geo-implementation/`. The four demo pages are maintained in `demos/` and published under `/demos/`. The next push to `main` republishes the site after Pages is active.

The contact form opens the visitor's email app with a prefilled draft. It does not store or transmit form data directly.
