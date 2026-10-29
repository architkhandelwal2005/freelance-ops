---
name: landing-page-build
description: Build a mobile-first landing page for an assigned product or campaign.
---

# landing-page-build

Use with `delivery-standards` for any assigned paid job. Work from Claude's job file, not from assumptions.

## Intake
Require Audience, offer, approved claims, copy/assets, conversion action, brand rules, hosting access and consent text. If a field is absent, put the precise question in the job file under `## Questions` for Claude. Do not fill missing client facts from search.

## Method and default stack
Default no-cost stack: Static HTML/CSS/JS with local preview and GitHub Pages; alternatives Astro or client CMS.

1. Map one goal and section outline from approved facts.
2. Draft plain copy with claim placeholders, then build semantic HTML.
3. Implement responsive CSS, accessible form/CTA and SEO metadata.
4. Test links, form route, keyboard and narrow screens.
5. Record Lighthouse mobile result and package source plus update guide.

## Time guide
Small 4-8 h; medium 1-2 days; large 3-5 days after assets. These are internal effort guides, not client commitments.

## QA: pass criteria
- [ ] Mobile Lighthouse performance >=90 on deployed page or documented blocker.
- [ ] No invented proof or claims.
- [ ] All links and CTA work.
- [ ] Keyboard focus and alt text pass.
- [ ] No horizontal overflow at 360px.

Save the evidence in the job folder; a claim of "tested" without results does not pass. Use [checklist.md](checklist.md) to record the checks.

## Deliverables and handover pack
Page source, live/staging URL when authorized, screenshots, QA log, update guide and walkthrough script. Include a plain-language `handover.md` with run/update steps, files, limits, backup location and a 60-second walkthrough script.

## Escalate to Claude when
Missing claim evidence, hosting credentials, live publish, paid asset or change to campaign scope. Record the question in the job file and stop the dependent action.

## Never
Never contact anyone or send client-facing work directly; Claude reviews and delivers. Never spend money or sign up as Archit; use no-cost tools first. Never invent clients, claims, results or experience; mark unknowns [TO CONFIRM]. Describe Archit as building with AI tools and checking every change by hand, never as hand-coding. Never confirm price, deadline or scope. Back up sites and work only on staging without written live-production go-ahead. Keep client data private; public samples use fictional brands. Do not put “free” in client-facing copy. Do not make unsupported medical, legal or financial claims.

For a fictional test brief, use [prompt.md](prompt.md).

Reusable starting file: [assets/index.html](assets/index.html). Adapt it to the approved job; sample facts are fictional.

