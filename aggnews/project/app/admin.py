"""The admin register of Aggregate News Web Application
-----------------------------

Project structure
-----------------
*aggnews/project/app/*
    **admin.py**:
        The admin register of Aggregate News Web Application

About this Module
------------------
The goal of this module is to register models of our Aggnews Web Application.
"""

__author__ = "Benoit Lapointe"
__date__ = "2021-03-19"
__copyright__ = "Copyright 2021, labesoft"
__version__ = "1.0.0"

from django.contrib import admin

from .models import *

admin.site.register(Headline)
