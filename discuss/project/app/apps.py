"""The app config module of Discussion Forum
-----------------------------

About this Module
------------------
The goal of this module is to map the app to be mapped directly to django
appconfig module.
"""

__author__ = "Benoit Lapointe"
__date__ = "2021-03-17"
__copyright__ = "Copyright 2021, labesoft"
__version__ = "1.0.0"

from django.apps import AppConfig

AppConfig.name = 'app'
