Status: To do | Priority: 1 | Deadline: 2 days

# 001 — Archit's portfolio website

## Goal
One fast, clean, mobile-first site that every pitch can link to. It must make a startup founder, D2C marketing head or agency owner think "this person can deliver".

## Must have
- Hero: name, positioning line (from AGENTS.md), one primary CTA (WhatsApp click-to-chat link to +91 98933 51932 with a prefilled "Hi Archit, I'd like to discuss a project" message) and a secondary CTA (email).
- Services (4 cards): AI automation; websites & landing pages; brand visibility (SEO + AI search / GEO); content & pitch decks. Each card: the outcome, 3 bullets, typical turnaround. No prices.
- Work / case studies (honest, factual):
  1. Sapcon Instruments — AI voice-notes-to-CRM automation (problem → what was built → result: "team is using it"). No confidential data.
  2. Live auction web app — real-time bidding used at Derma Cricket League 2026 and a FICCI FLO Indore event.
  3. Sample GEO audit (anonymised D2C brand) — what was checked and what it found.
  4. Demo projects from task 002 (link each).
- "How I work": AI tools + human checking, site backed up first, design kept, quick turnaround, white-label for agencies.
- About: BITS Pilani ECE, short and human.
- Contact: WhatsApp, email, LinkedIn. A simple contact form (Formspree-style or a Google Form link; no paid services).
- Basic SEO and AI-search hygiene on the portfolio itself: title, meta description, Open Graph image, JSON-LD (Person + ProfessionalService), sitemap.xml, robots.txt, llms.txt.

## Tech
Static site (plain HTML/CSS/JS or Astro/Next static export). Deploy on GitHub Pages or Vercel (no cost). Lighthouse mobile performance 90+.

## Acceptance criteria
- Live URL works on mobile; all links work; no invented facts; no prices.
- `portfolio/README.md` with the live URL and how to update case studies.
- Daily report with screenshots (desktop + mobile) and the 5-point summary.
