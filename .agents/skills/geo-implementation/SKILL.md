---
name: geo-implementation
description: Improve an assigned site’s machine-readable identity and AI-search discoverability.
---

# geo-implementation

Use with `delivery-standards` for any assigned paid job. Work from Claude's job file, not from assumptions.

## Intake
Require Canonical site URL, approved entity facts, existing crawl rules, CMS access, target questions and baseline observations. If a field is absent, put the precise question in the job file under `## Questions` for Claude. Do not fill missing client facts from search.

## Method and default stack
Default no-cost stack: Static JSON-LD, robots.txt, sitemap.xml and llms.txt; validate locally before staging.

1. Record current crawl/index and AI answer observations with prompts and dates.
2. Confirm entity, canonical URL and content from approved sources.
3. Add matching schema, crawl policy, sitemap, llms.txt and useful FAQ copy.
4. Validate schema and links; ensure robots does not block key pages.
5. Repeat the same visibility checks and report observed changes without rank promises.

## Time guide
Small 3-5 h; medium 1-2 days; large 3-5 days plus indexing time. These are internal effort guides, not client commitments.

## QA: pass criteria
- [ ] JSON-LD parses and matches visible facts.
- [ ] Canonical and sitemap URLs resolve.
- [ ] Robots syntax allows intended crawlers.
- [ ] FAQ answers are supported on-page.
- [ ] Before/after check uses identical prompts and states limits.

Save the evidence in the job folder; a claim of "tested" without results does not pass. Use [checklist.md](checklist.md) to record the checks.

## Deliverables and handover pack
Modified files, validation evidence, baseline/recheck sheet, source facts and handover script. Include a plain-language `handover.md` with run/update steps, files, limits, backup location and a 60-second walkthrough script.

## Escalate to Claude when
Unverified entity claims, production robots changes, access issues or visibility guarantees. Record the question in the job file and stop the dependent action.

## Never
Never contact anyone or send client-facing work directly; Claude reviews and delivers. Never spend money or sign up as Archit; use no-cost tools first. Never invent clients, claims, results or experience; mark unknowns [TO CONFIRM]. Describe Archit as building with AI tools and checking every change by hand, never as hand-coding. Never confirm price, deadline or scope. Back up sites and work only on staging without written live-production go-ahead. Keep client data private; public samples use fictional brands. Do not put “free” in client-facing copy. Do not make unsupported medical, legal or financial claims.

For a fictional test brief, use [prompt.md](prompt.md).

Reusable starting file: [assets/index.html](assets/index.html). Adapt it to the approved job; sample facts are fictional.

