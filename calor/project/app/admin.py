"""The admin module of The Calorie Calculator Web App
-----------------------------

About this Module
------------------
The goal of this module is to register all our models to admin site, Now we
can easily create/update on following UI: http://127.0.0.1:8000/admin/.
"""

__author__ = "Benoit Lapointe"
__date__ = "2021-03-17"
__copyright__ = "Copyright 2021, labesoft"
__version__ = "1.0.0"

from django.contrib import admin

from .models import *


class foodAdmin(admin.ModelAdmin):
    """The admin of the food model"""

    class Meta:
        model = Fooditem

    list_display = ['name']
    list_filter = ['name']


admin.site.register(Customer)
admin.site.register(UserFooditem)
admin.site.register(Category)
admin.site.register(Fooditem, foodAdmin)
