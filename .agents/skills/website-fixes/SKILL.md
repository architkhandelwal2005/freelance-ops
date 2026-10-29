---
name: website-fixes
description: Repair an assigned website defect while preserving layout and content.
---

# website-fixes

Use with `delivery-standards` for any assigned paid job. Work from Claude's job file, not from assumptions.

## Intake
Require Platform/version, exact defect and repro steps, staging access, source backup, target devices and acceptance check. If a field is absent, put the precise question in the job file under `## Questions` for Claude. Do not fill missing client facts from search.

## Method and default stack
Default no-cost stack: Browser dev tools and local copy; platform theme export; Lighthouse for measured speed changes.

1. Reproduce and capture before evidence.
2. Back up theme, database or source and verify restore path.
3. Find the narrow cause; patch staging without redesign.
4. Check desktop/mobile, keyboard, links and relevant browser paths.
5. Capture after evidence and prepare rollback instructions.

## Time guide
Small 2-4 h; medium 1 day; large 2-4 days after access. These are internal effort guides, not client commitments.

## QA: pass criteria
- [ ] Original failure reproduced before editing.
- [ ] Fix passes original repro on staging.
- [ ] No visible design drift or lost content.
- [ ] Mobile, keyboard and core path pass.
- [ ] Before/after evidence and rollback are present.

Save the evidence in the job folder; a claim of "tested" without results does not pass. Use [checklist.md](checklist.md) to record the checks.

## Deliverables and handover pack
Patch, before/after report, screenshots, backup path, rollback steps and walkthrough script. Include a plain-language `handover.md` with run/update steps, files, limits, backup location and a 60-second walkthrough script.

## Escalate to Claude when
Production access or deployment request, ambiguous regression, paid plugin, broken backup or design change. Record the question in the job file and stop the dependent action.

## Never
Never contact anyone or send client-facing work directly; Claude reviews and delivers. Never spend money or sign up as Archit; use no-cost tools first. Never invent clients, claims, results or experience; mark unknowns [TO CONFIRM]. Describe Archit as building with AI tools and checking every change by hand, never as hand-coding. Never confirm price, deadline or scope. Back up sites and work only on staging without written live-production go-ahead. Keep client data private; public samples use fictional brands. Do not put “free” in client-facing copy. Do not make unsupported medical, legal or financial claims.

For a fictional test brief, use [prompt.md](prompt.md).

Reusable starting file: [assets/after.html](assets/after.html). Adapt it to the approved job; sample facts are fictional.

