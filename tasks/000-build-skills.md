Status: Ready for Claude review | Priority: 1 | Deadline: 3 days

# 000 — Train yourself: build one skill per service

## Goal
For each service in AGENTS.md section 3, create a reusable skill so that a paid job can be delivered fast and to a professional standard, without Claude re-explaining anything.

## Where
`.agents/skills/<skill-name>/SKILL.md` in this repo (the location Codex loads repo skills from). If your Codex version loads skills from a different folder, put them there and mirror a copy here. Supporting files (prompts, checklists, starter code, scripts) go in the same skill folder.

## Skills to create (names fixed)
1. `delivery-standards` — the core skill every job uses: reading a job file, plan, backup, build, QA, handover pack, PR, report. Includes the honesty and safety rules from AGENTS.md.
2. `landing-page-build`
3. `website-fixes` (Shopify, WordPress, Webflow, custom)
4. `geo-implementation` (schema/JSON-LD, llms.txt, robots.txt for AI bots, sitemap/canonical, FAQ and "what we are" content, before/after AI-visibility check)
5. `ai-automation-build` (n8n, Make, Zapier, Google Apps Script, Python; AI steps with OpenAI/Claude APIs; Sheets/CRM; alerts)
6. `ai-chatbot-build` (website FAQ bot trained on site content with sources and human hand-off; WhatsApp bot via official WhatsApp Business Platform providers only)
7. `internal-tool-build` (dashboards, CRUD tools, MVPs on no-cost stacks)
8. `pitch-deck-build`
9. `content-writing` (website copy, blogs, founder LinkedIn ghostwriting, product listings for Shopify/Amazon/Flipkart)
10. `ad-creatives` (static ad concepts with copy and image prompts, hook/offer/CTA variants, short video scripts and shot lists)
11. `data-research` (public-source datasets, cleaning/dedup, competitor and market reports)
12. `short-form-video` (reels/shorts from long videos or raw footage: hook, cuts, captions, aspect ratio, batch of 10; no-cost tools such as CapCut, DaVinci Resolve, ffmpeg)
13. `faceless-video` (script, AI or stock visuals, voiceover, edit, thumbnail; copyright-safe assets only, licences recorded)
14. `social-media-content` (content calendars, post and carousel graphics, captions, newsletters)
15. `transcription-subtitles-voiceover` (transcripts, SRT, English/Hindi translation, voiceover tracks; accuracy-checked)
16. `case-study-writeup` (turning a finished job into an honest portfolio case study)

## Every SKILL.md must contain
- Frontmatter: `name`, `description` (one line: when to use it).
- **Intake:** what the job file must contain; questions to ask Claude if missing.
- **Step-by-step method**, with the default stack (no-cost tools first) and alternatives.
- **Time guide:** small / medium / large job estimates.
- **QA checklist** with pass criteria (e.g. Lighthouse mobile ≥ 90, all links work, schema validates, automation tested with 5 sample inputs, deck proofread, facts sourced).
- **Deliverables & handover pack:** what the client receives (files, live link, how-to doc, video script for a walkthrough, backup location).
- **Escalate to Claude when:** scope creep, paid tool needed, access missing, risk to a live site, anything client-facing.
- **Never list:** the rules from AGENTS.md section 4 that matter for this service.

## Prove each skill works
For each skill, run it once on a fictional brand and save the output in `deliverables/samples/<skill-name>/` (this also covers task 005). Keep each sample small but real (working code, real deck file, real copy).

## Acceptance criteria
- 16 skills exist, each loadable, each with all sections above.
- 16 samples exist, each passing its own QA checklist.
- `reports/daily_YYYY-MM-DD.md` lists every skill, its sample path, and what you'd still improve.
- Pull request opened; Claude reviews before merge.
