// Google Apps Script starter. DRY_RUN stays true until Claude approves credentials,
// consent, recipients and production trigger. Never paste secrets into this file.
const DRY_RUN = true;

function handleEnquiry(payload) {
  const required = ['id', 'name', 'email', 'message'];
  for (const field of required) if (!payload[field]) throw new Error('Missing ' + field);
  if (!/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(payload.email)) throw new Error('Invalid email');
  const row = [payload.id, new Date().toISOString(), payload.name, payload.email, payload.message];
  if (DRY_RUN) return { status: 'preview', row, alert: 'New enquiry: ' + payload.id };
  const props = PropertiesService.getScriptProperties();
  const sheetId = props.getProperty('SHEET_ID');
  const owner = props.getProperty('OWNER_EMAIL');
  if (!sheetId || !owner) throw new Error('Approved configuration missing');
  const sheet = SpreadsheetApp.openById(sheetId).getSheetByName('Enquiries');
  if (!sheet) throw new Error('Enquiries tab missing');
  const existing = sheet.createTextFinder(payload.id).matchEntireCell(true).findNext();
  if (existing) return { status: 'duplicate', id: payload.id };
  sheet.appendRow(row);
  MailApp.sendEmail(owner, 'New enquiry', 'A new enquiry was recorded: ' + payload.id);
  return { status: 'recorded', id: payload.id };
}
