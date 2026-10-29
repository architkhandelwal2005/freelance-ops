---
name: transcription-subtitles-voiceover
description: Deliver checked transcripts, timed subtitles and permitted voice tracks.
---

# transcription-subtitles-voiceover

Use with `delivery-standards` for any assigned paid job. Work from Claude's job file, not from assumptions.

## Intake
Require Source audio rights, languages, speaker names, terminology, format, timecode style and voice consent. If a field is absent, put the precise question in the job file under `## Questions` for Claude. Do not fill missing client facts from search.

## Method and default stack
Default no-cost stack: Manual correction with SRT and WAV; local transcription/TTS only when available and permitted.

1. Listen to whole source and note speakers/unclear terms.
2. Transcribe verbatim or clean style as requested.
3. Time SRT cues to speech and line length.
4. Translate meaning with specialist terms checked; record voice only with consent.
5. Replay audio against SRT and export requested formats.

## Time guide
Small 2-4 h per 10 minutes; medium 1 day; large 2+ days after audio. These are internal effort guides, not client commitments.

## QA: pass criteria
- [ ] Transcript checked against full source.
- [ ] SRT timestamps ascend without overlap.
- [ ] No invented words in unclear audio.
- [ ] Translation preserves meaning.
- [ ] Voice track plays cleanly and has consent.

Save the evidence in the job folder; a claim of "tested" without results does not pass. Use [checklist.md](checklist.md) to record the checks.

## Deliverables and handover pack
TXT/DOCX transcript, SRT, translation, WAV/MP3 if requested, terminology notes and walkthrough script. Include a plain-language `handover.md` with run/update steps, files, limits, backup location and a 60-second walkthrough script.

## Escalate to Claude when
Unclear critical speech, consent missing, sensitive recording or requested voice imitation. Record the question in the job file and stop the dependent action.

## Never
Never contact anyone or send client-facing work directly; Claude reviews and delivers. Never spend money or sign up as Archit; use no-cost tools first. Never invent clients, claims, results or experience; mark unknowns [TO CONFIRM]. Describe Archit as building with AI tools and checking every change by hand, never as hand-coding. Never confirm price, deadline or scope. Back up sites and work only on staging without written live-production go-ahead. Keep client data private; public samples use fictional brands. Do not put “free” in client-facing copy. Do not make unsupported medical, legal or financial claims.

For a fictional test brief, use [prompt.md](prompt.md).
