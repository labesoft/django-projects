"""The forms of the Job Portal Web Application
-----------------------------

About this Module
------------------
The goal of this module is to manage the logic of the forms that candidate will
fill in order to complete a job application.
"""

__author__ = "Benoit Lapointe"
__date__ = "2021-03-24"
__copyright__ = "Copyright 2021, labesoft"
__version__ = "1.0.0"

from django.forms import ModelForm

from .models import *


class ApplyForm(ModelForm):
    class Meta:
        model = Candidates
        fields = "__all__"
