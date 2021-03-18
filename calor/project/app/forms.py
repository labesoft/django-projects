"""The forms of The Calorie Calculator Web App
-----------------------------

About this Module
------------------
The goal of this module is manage forms in a simple manner using all fields of
models to create, update models which we have created earlier in models.py
(for CRUD functionality).
"""

__author__ = "Benoit Lapointe"
__date__ = "2021-03-17"
__copyright__ = "Copyright 2021, labesoft"
__version__ = "1.0.0"

from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

from .models import *


class FooditemForm(ModelForm):
    """The form for a food item"""

    class Meta:
        model = Fooditem
        fields = "__all__"


class AddUserFooditem(ModelForm):
    """The form to add food item for a user"""

    class Meta:
        model = UserFooditem
        fields = "__all__"


class CreateUserForm(UserCreationForm):
    """The form to create a new user"""

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
