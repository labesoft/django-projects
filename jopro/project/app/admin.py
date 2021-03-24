"""The administration of the Job Portal Web Application
-----------------------------

About this Module
------------------
The goal of this module is to register the models to the web application
admin site.
"""

__author__ = "Benoit Lapointe"
__date__ = "2021-03-24"
__copyright__ = "Copyright 2021, labesoft"
__version__ = "1.0.0"

from django.contrib import admin

from .models import *

# Register your models here.
admin.site.register(Company)
admin.site.register(Candidate)
admin.site.register(JobOffer)
