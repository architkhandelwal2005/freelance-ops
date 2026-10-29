# Backup and restore record

Job: [TO CONFIRM]  
Environment: [TO CONFIRM: staging or approved production]  
Backup time and timezone: [TO CONFIRM]  
Source revision/version: [TO CONFIRM]  
Backup storage path: [TO CONFIRM]  
Restore owner: [TO CONFIRM]

1. Export the source files and database if present. For hosted tools, use the platform's version/snapshot feature.
2. Verify the backup exists and can be read. Record file counts and a checksum where practical.
3. Make changes on staging or a copy. Preserve original assets and database.
4. To roll back, stop edits, restore the saved revision and data, then rerun the original acceptance path.
5. Record who approved any production change in the job file. Never treat a backup as permission to deploy.
