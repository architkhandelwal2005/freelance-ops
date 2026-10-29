---
name: ai-automation-build
description: Build and test a small assigned workflow from intake to record and alert.
---

# ai-automation-build

Use with `delivery-standards` for any assigned paid job. Work from Claude's job file, not from assumptions.

## Intake
Require Trigger, fields, consent, destinations, error owner, five representative cases, credentials and retention requirements. If a field is absent, put the precise question in the job file under `## Questions` for Claude. Do not fill missing client facts from search.

## Method and default stack
Default no-cost stack: Python standard library or Google Apps Script with test fixtures; n8n/Make/Zapier only if already available.

1. Draw trigger, transform, storage, notification and failure paths.
2. Define field schema, idempotency key and privacy boundary.
3. Build on a copy with secrets outside source; mock paid AI calls.
4. Test five cases including missing, duplicate and malformed input.
5. Document retries, alerts, manual fallback and credential handover.

## Time guide
Small 4-8 h; medium 1-3 days; large 4+ days after integration access. These are internal effort guides, not client commitments.

## QA: pass criteria
- [ ] Five test inputs have expected outputs.
- [ ] Duplicates do not create extra records.
- [ ] Bad input fails safely with clear log.
- [ ] No secrets in files or logs.
- [ ] A non-technical operator can run fallback.

Save the evidence in the job folder; a claim of "tested" without results does not pass. Use [checklist.md](checklist.md) to record the checks.

## Deliverables and handover pack
Flow/source, config template, five-case results, runbook, sample records and walkthrough script. Include a plain-language `handover.md` with run/update steps, files, limits, backup location and a 60-second walkthrough script.

## Escalate to Claude when
Paid API, personal data transfer, live credentials, unclear consent, production trigger or quota risk. Record the question in the job file and stop the dependent action.

## Never
Never contact anyone or send client-facing work directly; Claude reviews and delivers. Never spend money or sign up as Archit; use no-cost tools first. Never invent clients, claims, results or experience; mark unknowns [TO CONFIRM]. Describe Archit as building with AI tools and checking every change by hand, never as hand-coding. Never confirm price, deadline or scope. Back up sites and work only on staging without written live-production go-ahead. Keep client data private; public samples use fictional brands. Do not put “free” in client-facing copy. Do not make unsupported medical, legal or financial claims.

For a fictional test brief, use [prompt.md](prompt.md).

Reusable starting file: [assets/workflow.py](assets/workflow.py). Adapt it to the approved job; sample facts are fictional.

