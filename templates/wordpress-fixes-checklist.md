# WordPress website-fix checklist

## Intake
- [ ] Claude's job file names the exact bug, page URL, expected behavior, browser/device and staging access.
- [ ] Confirm WordPress, PHP, theme and relevant plugin versions from the assigned site. Record only in the private job file.
- [ ] Confirm written permission before any live production change.

## Protect the original
- [ ] Export database and `wp-content` or take a host snapshot on the approved environment.
- [ ] Record backup time, storage path and restore steps. Test a restore on staging if the change is material.
- [ ] Capture the defect before editing. Preserve the existing design and content.

## Fix on staging
- [ ] Reproduce the defect. Check console/server errors and recent changes before editing.
- [ ] Change the narrowest responsible theme, plugin or configuration layer. Use a child theme when changing theme code.
- [ ] Avoid editing WordPress core or a vendor plugin directly; updates would overwrite it.
- [ ] Run the original reproduction path, a mobile check, keyboard navigation, forms and checkout if affected.
- [ ] Record before/after evidence and a rollback command or restore procedure.

## Handover
- [ ] Provide changed files, backup location, test evidence, any remaining risk and a short maintenance note to Claude.
- [ ] Claude reviews before client exposure or production deployment.
