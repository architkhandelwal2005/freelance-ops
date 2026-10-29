---
name: delivery-standards
description: Run the intake, protected build, review and handover process for any assigned job.
---

# delivery-standards

Use this core process for every assigned paid job. Work from Claude's job file, not from assumptions.

## Intake
Require Claude job file, scope, acceptance criteria, source assets, access level, public-use permission and reviewer. If a field is absent, put the precise question in the job file under `## Questions` for Claude. Do not fill missing client facts from search.

## Method and default stack
Default no-cost stack: Git branch, local files, Markdown checklist and screenshots; use an isolated staging copy.

1. Read AGENTS.md, CONTEXT.md and the job file; mark missing facts [TO CONFIRM].
2. Write plan and acceptance checks in the job file; save a dated backup before edits.
3. Build only the agreed scope on a job branch, using fictional data for tests.
4. Run the service skill QA and record evidence, defects and limitations.
5. Package source, output, backup, update notes and walkthrough script; open a pull request for Claude.

## Time guide
Small 1-2 h; medium 0.5-1 day; large 2+ days, pending Claude scope. These are internal effort guides, not client commitments.

## QA: pass criteria
- [ ] Job file has all required fields and plan.
- [ ] Backup is restorable and original untouched.
- [ ] Each acceptance criterion has evidence.
- [ ] No client data leaks into sample or public artifact.
- [ ] PR and handover identify known limits.

Save the evidence in the job folder; a claim of "tested" without results does not pass. Use [checklist.md](checklist.md) to record the checks.

## Deliverables and handover pack
Job folder, backup manifest, QA evidence, handover.md, walkthrough script, PR and daily report. Include a plain-language `handover.md` with run/update steps, files, limits, backup location and a 60-second walkthrough script.

## Escalate to Claude when
Any missing permission, client-facing release, scope, price, deadline, security or live-production concern. Record the question in the job file and stop the dependent action.

## Never
Never contact anyone or send client-facing work directly; Claude reviews and delivers. Never spend money or sign up as Archit; use no-cost tools first. Never invent clients, claims, results or experience; mark unknowns [TO CONFIRM]. Describe Archit as building with AI tools and checking every change by hand, never as hand-coding. Never confirm price, deadline or scope. Back up sites and work only on staging without written live-production go-ahead. Keep client data private; public samples use fictional brands. Do not put “free” in client-facing copy. Do not make unsupported medical, legal or financial claims.

For a fictional test brief, use [prompt.md](prompt.md).
