This is a database migration repository.

More information at
http://code.google.com/p/sqlalchemy-migrate/


Set your settings first:
```bash
export SETTINGS="app.settings.develop"
```

Initialize migrations:
```bash
python app/migrations/manage.py version_control
```

Check the current version:
```bash
python app/migrations/manage.py version
```

Add a new migration script:
```bash
python app/migrations/manage.py script "initial"
```

Test the created migration script:
```bash
python app/migrations/manage.py test
```

Upgrade the database:
```bash
python app/migrations/manage.py upgrade
```

Downgrade the database to the version:
```bash
python app/migrations/manage.py downgrade 001
```
