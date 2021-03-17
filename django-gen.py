"""A small script to generate Django Apps
-----------------------------

About this module
-----------------
This module generates django apps for all sub-project located in this main
project
"""

__author__ = "Benoit Lapointe"
__date__ = "2021-03-15"
__copyright__ = "Copyright 2021, Benoit Lapointe"
__version__ = "1.0.0"

import os
import subprocess

if __name__ == '__main__':
    root_path = os.path.dirname(__file__)
    django_dir = "project"
    app_dir = "app"

    for dir in os.listdir("."):
        if os.path.isdir(dir) and "__init__.py" in (os.listdir(dir)):
            # Create django project
            os.chdir(dir)
            subprocess.run(["django-admin", "startproject", django_dir])

            # Create django app
            os.chdir(django_dir)
            subprocess.run(["django-admin", "startapp", app_dir])

            # Go back to this script file path
            os.chdir(root_path)
