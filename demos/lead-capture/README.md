# Nila Studio enquiry flow (fictional demo)

Open `index.html` in a browser. Submit a fictional enquiry and inspect the local row count, owner alert and reply previews. Download the rows as CSV; they can be imported into a Google Sheet. Nothing is sent or uploaded.

Run `python flow.py` to exercise the five-case backend contract. Expected result: `(3, 6, 1)` for records, message previews and rejected inputs. `records.csv` and `outbox.json` are created. `flow.json` records the intended form-to-Sheet-to-alert/reply nodes. A real Sheet or message channel needs approved access, consent, and Claude's review.

**60-second walkthrough:** submit the form, show the two immediate previews and CSV, then run the Python script and show duplicate/invalid handling.
