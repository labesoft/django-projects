"""The Model of the Calorie Calculator Web Application
-----------------------------

About this Module
------------------
The goal of this module is to implement the business logic of a calorie
calculator application.
"""

__author__ = "Benoit Lapointe"
__date__ = "2021-03-17"
__copyright__ = "Copyright 2021, labesoft"
__version__ = "1.0.0"

from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    """This model is used to store customer informations"""
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        """The string object of a customer based on his name"""
        return str(self.name)


class Category(models.Model):
    """This model is used to store category items of food we offer"""
    options = (
        ('breakfast', 'breakfast'),
        ('lunch', 'lunch'),
        ('dinner', 'dinner'),
        ('snacks', 'snacks'),
    )
    name = models.CharField(max_length=50, choices=options)

    def __str__(self):
        """The string object of a category based on its name"""
        return self.name


class Fooditem(models.Model):
    """This model is used to store"""
    name = models.CharField(max_length=200)
    category = models.ManyToManyField(Category)
    carbohydrate = models.DecimalField(max_digits=5, decimal_places=2,
                                       default=0)
    fats = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    protein = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    calorie = models.DecimalField(max_digits=5, decimal_places=2, default=0,
                                  blank=True)
    quantity = models.IntegerField(default=1, null=True, blank=True)

    def __str__(self):
        """The string object of a food item based on its name"""
        return str(self.name)


class UserFooditem(models.Model):
    """This model is used for the user page"""
    customer = models.ManyToManyField(Customer, blank=True)
    fooditem = models.ManyToManyField(Fooditem)
