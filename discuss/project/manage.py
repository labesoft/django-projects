#!/usr/bin/env python
"""The Main Application of The Discussion Forum
-----------------------------

About this Module
------------------
This module is the main entry point of The Main Application of The Discussion
Forum. This is also Django's command-line utility for administrative tasks.

"""

__author__ = "Benoit Lapointe"
__date__ = "2021-03-14"
__copyright__ = "Copyright 2021, labesoft"
__version__ = "1.0.0"

import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    """Main entry point of discuss"""
    main()
