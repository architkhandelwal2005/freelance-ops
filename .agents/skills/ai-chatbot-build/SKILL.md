---
name: ai-chatbot-build
description: Build a grounded website FAQ bot with citations and human handoff.
---

# ai-chatbot-build

Use with `delivery-standards` for any assigned paid job. Work from Claude's job file, not from assumptions.

## Intake
Require Approved source pages, FAQs, prohibited advice, handoff route, privacy notice and channel permissions. If a field is absent, put the precise question in the job file under `## Questions` for Claude. Do not fill missing client facts from search.

## Method and default stack
Default no-cost stack: Local curated FAQ JSON and accessible widget; official WhatsApp Business provider only for WhatsApp.

1. Collect approved pages and record source URL plus revision.
2. Build retrieval over answerable questions and an explicit confidence threshold.
3. Display source and decline/handoff for unsupported questions.
4. Test normal, ambiguous, prompt-injection and unsafe cases.
5. Package content refresh steps and operator handoff.

## Time guide
Small 4-8 h; medium 1-3 days; large 4+ days with channel integration. These are internal effort guides, not client commitments.

## QA: pass criteria
- [ ] Answers cite an approved source.
- [ ] Unknown questions hand off without invention.
- [ ] Prompt injection cannot override instructions.
- [ ] Widget works by keyboard and mobile.
- [ ] No unofficial WhatsApp automation.

Save the evidence in the job folder; a claim of "tested" without results does not pass. Use [checklist.md](checklist.md) to record the checks.

## Deliverables and handover pack
Widget/source, knowledge file, test transcript, handoff route, update guide and walkthrough script. Include a plain-language `handover.md` with run/update steps, files, limits, backup location and a 60-second walkthrough script.

## Escalate to Claude when
WhatsApp provider access, regulated advice, missing source rights, personal data or live publish. Record the question in the job file and stop the dependent action.

## Never
Never contact anyone or send client-facing work directly; Claude reviews and delivers. Never spend money or sign up as Archit; use no-cost tools first. Never invent clients, claims, results or experience; mark unknowns [TO CONFIRM]. Describe Archit as building with AI tools and checking every change by hand, never as hand-coding. Never confirm price, deadline or scope. Back up sites and work only on staging without written live-production go-ahead. Keep client data private; public samples use fictional brands. Do not put “free” in client-facing copy. Do not make unsupported medical, legal or financial claims.

For a fictional test brief, use [prompt.md](prompt.md).

Reusable starting file: [assets/widget.html](assets/widget.html). Adapt it to the approved job; sample facts are fictional.

