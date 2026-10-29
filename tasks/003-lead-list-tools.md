Status: To do | Priority: 3 | Deadline: 5 days

# 003 — Lead-list tools

Build scripts in `tools/` that turn public sources into clean CSVs (respect robots.txt and terms; no logins, no paid APIs):
1. Agency finder: Clutch / GoodFirms / DesignRush / Shopify & Spur partner directories for India → agency name, city, size band, services, website, public contact page URL.
2. Startup funding watcher: Inc42 / Entrackr / YourStory funding round-ups → startup, round, amount, date, sector, founders named in the article, website.
3. Founder/contact enricher: given a website, find the About/Team/Contact pages and extract named founders and publicly listed emails/phones (only what is printed on the site; never guess).
4. Dedupe step against `leads/claude_leads_do_not_contact.csv` and `leads/codex_leads.csv`.

Output: `leads/raw_*.csv`. Claude imports Agency/Startup/D2C rows into the master sheet; you keep area A–K rows in `leads/codex_leads.csv`.
