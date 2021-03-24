"""The apps of the Job Portal Web Application
-----------------------------

Project structure
-----------------
*jopro/project/app/*
    **apps.py**:
        The apps of the Job Portal Web Application

About this Module
------------------
The goal of this module is to map the models to the installed apps.
"""

__author__ = "Benoit Lapointe"
__date__ = "2021-03-24"
__copyright__ = "Copyright 2021, labesoft"
__version__ = "1.0.0"

from django.apps import AppConfig

AppConfig.name = 'app'
