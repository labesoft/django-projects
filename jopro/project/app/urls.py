"""The urls of app side of the Job Portal web application
-----------------------------

About this Module
------------------
The goal of this module is to register urls to the views of the application.
"""

__author__ = "Benoit Lapointe"
__date__ = "2021-03-24"
__copyright__ = "Copyright 2021, labesoft"
__version__ = "1.0.0"

from django.urls import path

from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('login/', site_login, name='login'),
    path('logout/', site_logout, name='logout'),
    path('register/', register, name='register'),
    path('job-offer/', job_offer, name='job-offer'),
    path('apply/', apply, name='apply'),
]
