---
name: pitch-deck-build
description: Prepare a sourced investor or sales deck from an approved brief.
---

# pitch-deck-build

Use with `delivery-standards` for any assigned paid job. Work from Claude's job file, not from assumptions.

## Intake
Require Audience, purpose, approved claims and metrics, brand assets, slide count, editable format and source list. If a field is absent, put the precise question in the job file under `## Questions` for Claude. Do not fill missing client facts from search.

## Method and default stack
Default no-cost stack: python-pptx for editable PPTX or Google Slides if already connected; PDF for review.

1. Write a one-line narrative and slide outline.
2. Map each claim to source or [TO CONFIRM].
3. Create legible charts and slide layouts with consistent typography.
4. Proofread numbers, labels and visual hierarchy.
5. Export review PDF and check every slide visually.

## Time guide
Small 4-8 h; medium 1-2 days; large 3-5 days after data. These are internal effort guides, not client commitments.

## QA: pass criteria
- [ ] All factual claims have sources.
- [ ] No invented traction or market size.
- [ ] All slides readable at presentation size.
- [ ] Editable file opens and PDF renders.
- [ ] Narrative and call to action match brief.

Save the evidence in the job folder; a claim of "tested" without results does not pass. Use [checklist.md](checklist.md) to record the checks.

## Deliverables and handover pack
Editable deck, review PDF, sources/claim log, speaker notes and walkthrough script. Include a plain-language `handover.md` with run/update steps, files, limits, backup location and a 60-second walkthrough script.

## Escalate to Claude when
Missing metrics, financial/market claims, investor commitments or changed narrative. Record the question in the job file and stop the dependent action.

## Never
Never contact anyone or send client-facing work directly; Claude reviews and delivers. Never spend money or sign up as Archit; use no-cost tools first. Never invent clients, claims, results or experience; mark unknowns [TO CONFIRM]. Describe Archit as building with AI tools and checking every change by hand, never as hand-coding. Never confirm price, deadline or scope. Back up sites and work only on staging without written live-production go-ahead. Keep client data private; public samples use fictional brands. Do not put “free” in client-facing copy. Do not make unsupported medical, legal or financial claims.

For a fictional test brief, use [prompt.md](prompt.md).
