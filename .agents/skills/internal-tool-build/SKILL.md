---
name: internal-tool-build
description: Build a small assigned dashboard or CRUD tool on a no-cost stack.
---

# internal-tool-build

Use with `delivery-standards` for any assigned paid job. Work from Claude's job file, not from assumptions.

## Intake
Require Users, records, fields, access roles, sample data, export need, hosting and retention policy. If a field is absent, put the precise question in the job file under `## Questions` for Claude. Do not fill missing client facts from search.

## Method and default stack
Default no-cost stack: Local HTML/JS with JSON or SQLite; alternatives Streamlit or existing database.

1. Define entities, permissions and exact user actions.
2. Build smallest usable create/read/update/search flow on fictional data.
3. Validate input, empty/error states and export.
4. Test desktop/mobile and persistence boundaries.
5. Package schema, migration/backup notes and operator guide.

## Time guide
Small 1 day; medium 2-4 days; large 1+ week after scope. These are internal effort guides, not client commitments.

## QA: pass criteria
- [ ] Create/edit/search work on test records.
- [ ] Invalid input is rejected clearly.
- [ ] No sensitive data in public demo.
- [ ] Persistence limits are documented.
- [ ] Keyboard and narrow-screen path work.

Save the evidence in the job folder; a claim of "tested" without results does not pass. Use [checklist.md](checklist.md) to record the checks.

## Deliverables and handover pack
Runnable app, sample data, schema, QA log, backup/export guide and walkthrough script. Include a plain-language `handover.md` with run/update steps, files, limits, backup location and a 60-second walkthrough script.

## Escalate to Claude when
Authentication/security expectations, real data, production hosting, scope growth or paid backend. Record the question in the job file and stop the dependent action.

## Never
Never contact anyone or send client-facing work directly; Claude reviews and delivers. Never spend money or sign up as Archit; use no-cost tools first. Never invent clients, claims, results or experience; mark unknowns [TO CONFIRM]. Describe Archit as building with AI tools and checking every change by hand, never as hand-coding. Never confirm price, deadline or scope. Back up sites and work only on staging without written live-production go-ahead. Keep client data private; public samples use fictional brands. Do not put “free” in client-facing copy. Do not make unsupported medical, legal or financial claims.

For a fictional test brief, use [prompt.md](prompt.md).

Reusable starting file: [assets/index.html](assets/index.html). Adapt it to the approved job; sample facts are fictional.

