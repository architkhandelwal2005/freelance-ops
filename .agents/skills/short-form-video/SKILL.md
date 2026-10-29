---
name: short-form-video
description: Edit approved footage into vertical clips with captions and hooks.
---

# short-form-video

Use with `delivery-standards` for any assigned paid job. Work from Claude's job file, not from assumptions.

## Intake
Require Footage rights, selected moments, aspect/length, caption language, brand kit, output count and revision limits. If a field is absent, put the precise question in the job file under `## Questions` for Claude. Do not fill missing client facts from search.

## Method and default stack
Default no-cost stack: ffmpeg with local subtitle files; alternatives CapCut or DaVinci Resolve if installed.

1. Log source rights and select moments from approved footage.
2. Cut for an immediate hook and one idea per clip.
3. Create timed captions and safe-area layout.
4. Export 1080x1920 MP4 plus thumbnail.
5. Watch every export with sound and check caption sync.

## Time guide
Small 2-4 h per clip; medium 1-2 days for 5; large 3-5 days for 10. These are internal effort guides, not client commitments.

## QA: pass criteria
- [ ] Playable vertical video at requested resolution.
- [ ] Captions match speech and timing.
- [ ] No clipped faces or text.
- [ ] Audio peaks do not distort.
- [ ] Rights and source timestamps recorded.

Save the evidence in the job folder; a claim of "tested" without results does not pass. Use [checklist.md](checklist.md) to record the checks.

## Deliverables and handover pack
MP4 clips, SRT, thumbnails, edit decision list, licence log and walkthrough script. Include a plain-language `handover.md` with run/update steps, files, limits, backup location and a 60-second walkthrough script.

## Escalate to Claude when
Missing footage rights, paid music, poor audio, new clip count or public upload. Record the question in the job file and stop the dependent action.

## Never
Never contact anyone or send client-facing work directly; Claude reviews and delivers. Never spend money or sign up as Archit; use no-cost tools first. Never invent clients, claims, results or experience; mark unknowns [TO CONFIRM]. Describe Archit as building with AI tools and checking every change by hand, never as hand-coding. Never confirm price, deadline or scope. Back up sites and work only on staging without written live-production go-ahead. Keep client data private; public samples use fictional brands. Do not put “free” in client-facing copy. Do not make unsupported medical, legal or financial claims.

For a fictional test brief, use [prompt.md](prompt.md).
