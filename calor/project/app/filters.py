"""The search filters of The Calorie Calculator Web Application
-----------------------------

About this Module
------------------
The goal of this module is to enables search filter for the user.
"""

__author__ = "Benoit Lapointe"
__date__ = "2021-03-17"
__copyright__ = "Copyright 2021, labesoft"
__version__ = "1.0.0"

import django_filters

from .models import *


class fooditemFilter(django_filters.FilterSet):
    """The filter for a food item"""
    class Meta:
        model = Fooditem
        fields = ['name']
