"""The forms of the Discussion Forum Web Application
-----------------------------
        
About this module
-----------------
This module is used for creating, updating various models that we have
created in models.py (for CRUD functionality). We use here inbuilt Django forms.

It contains two forms one for creating a new forum and one for adding views
to the existing forum, which is clear from the models which we are using in
Meta class (a metaclass is used to define an extra option for a model or form so
that other classes within the web app know the capabilities of the model)
"""

__author__ = "Benoit Lapointe"
__date__ = "2021-03-15"
__copyright__ = "Copyright 2021, Benoit Lapointe"
__version__ = "1.0.0"

from django.forms import ModelForm
from .models import *


class CreateInForum(ModelForm):
    """The form which creates a new forum"""
    class Meta:
        model = Forum
        fields = "__all__"


class CreateInDiscussion(ModelForm):
    """The form which adds views to the existing forum"""
    class Meta:
        model = Discussion
        fields = "__all__"
