# Nila Studio FAQ assistant (fictional demo)

Run `python build_index.py`, then open `index.html`. The crawler follows links from `pages/index.html` only within `pages/`, extracts two approved FAQ answers, and writes `knowledge.json` plus a browser-loadable `knowledge.js`. Ask “Is Nila Studio a real shop?” or “What does Nila Studio make?” to see an answer with a source. An unsupported or instruction-injection question returns a human handoff. No AI API or WhatsApp account is used.

This is an embeddable local FAQ widget with a deterministic retrieval rule. A paid job would need client-approved source pages, privacy review, larger question tests, and a real human handoff destination.

**60-second walkthrough:** run the crawler; show its two source pages, ask a known question and open its citation, then ask an unknown question and show the handoff.
