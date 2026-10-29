# Automation starters

- `form-sheet-alert.gs`: form payload to a Google Sheet and owner alert. It defaults to preview mode. Real use needs approved script properties, a configured Sheet, consent and a reviewed trigger.
- `email-ai-task.py`: parses the fictional `sample.eml`, creates a local summary/task preview, and makes no inbox or AI API call. Replace the summary function only after Claude approves the provider, data transfer and quality checks.
- `whatsapp-enquiry-crm.json`: an integration design for the official WhatsApp Business Platform or an approved provider. It includes signature verification, deduplication, CRM fields and failure handling; it is not an unofficial WhatsApp bot.

Test five representative cases, including duplicate, missing field and failure paths, before delivery. Do not activate a live trigger or send any message without written job approval and Claude review.
