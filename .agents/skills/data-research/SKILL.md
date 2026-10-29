---
name: data-research
description: Produce a clean public-source dataset and concise research findings.
---

# data-research

Use with `delivery-standards` for any assigned paid job. Work from Claude's job file, not from assumptions.

## Intake
Require Research questions, geography, fields, source rules, freshness date, exclusions and output format. If a field is absent, put the precise question in the job file under `## Questions` for Claude. Do not fill missing client facts from search.

## Method and default stack
Default no-cost stack: Python csv/pandas and source URLs; public pages only, no access bypass.

1. Define inclusion criteria and field dictionary.
2. Collect only public permissible records with source and date.
3. Normalize, deduplicate and flag unknowns.
4. Validate counts and sample against original sources.
5. Write findings with caveats and reproducible method.

## Time guide
Small 3-6 h; medium 1-3 days; large 1+ week after source scope. These are internal effort guides, not client commitments.

## QA: pass criteria
- [ ] Every row has provenance.
- [ ] No personal data harvesting.
- [ ] Duplicates and nulls counted.
- [ ] Findings match dataset.
- [ ] Source terms and robots respected.

Save the evidence in the job folder; a claim of "tested" without results does not pass. Use [checklist.md](checklist.md) to record the checks.

## Deliverables and handover pack
CSV, field dictionary, source log, QA summary, report and walkthrough script. Include a plain-language `handover.md` with run/update steps, files, limits, backup location and a 60-second walkthrough script.

## Escalate to Claude when
Restricted source, sensitive data, uncertain rights or expanded data fields. Record the question in the job file and stop the dependent action.

## Never
Never contact anyone or send client-facing work directly; Claude reviews and delivers. Never spend money or sign up as Archit; use no-cost tools first. Never invent clients, claims, results or experience; mark unknowns [TO CONFIRM]. Describe Archit as building with AI tools and checking every change by hand, never as hand-coding. Never confirm price, deadline or scope. Back up sites and work only on staging without written live-production go-ahead. Keep client data private; public samples use fictional brands. Do not put “free” in client-facing copy. Do not make unsupported medical, legal or financial claims.

For a fictional test brief, use [prompt.md](prompt.md).

Reusable starting file: [assets/clean.py](assets/clean.py). Adapt it to the approved job; sample facts are fictional.

