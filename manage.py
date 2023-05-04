#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from django.conf import settings
from django.db.migrations import AlterField


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myblog.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    # below lines are to avoid the errors while migrating new modules into Mongo DB.
    if sys.argv[1] == 'migrate':
        if settings.DATABASES['default']['ENGINE'] == 'djongo':
            AlterField.database_forwards = lambda *_: None
            AlterField.database_backwards = lambda *_: None
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
