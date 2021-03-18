"""The Tests of the Calorie Calculator Web Application
-----------------------------

About this Module
------------------
The goal of this module is to test the views and the models of the Calorie
Calculator Web Application.
"""

__author__ = "Benoit Lapointe"
__date__ = "2021-03-18"
__copyright__ = "Copyright 2021, labesoft"
__version__ = "1.0.0"

# Create your tests here.
from unittest import TestCase
from unittest.mock import MagicMock

from app.models import Fooditem, Customer, Category
from django.contrib.auth.models import User


def create_fooditem(name):
    """Utility function to create a Fooditem usable for views tests

    :param name: models.CharField(max_length=200)
    :category: models.ManyToManyField(Category)
    :carbohydrate: models.DecimalField(max_digits=5, decimal_places=2,
                default=0)
    :fats: models.DecimalField(max_digits=5, decimal_places=2, default=0)
    :protein: models.DecimalField(max_digits=5, decimal_places=2, default=0)
    :calorie: models.DecimalField(max_digits=5, decimal_places=2, default=0,
           blank=True)
    :quantity: models.IntegerField(default=1, null=True, blank=True)
    :return: the Fooditem object created with name, category, carbohydrate,
          fats, protein, calorie, quantity
    """
    return Fooditem.objects.create(name=name)


def create_customer(name, user):
    """Utility function to create a Customer usable for views tests

    :param name: models.CharField(max_length=200, null=True)
    :param user: from models.OneToOneField(User, null=True,
            on_delete=models.CASCADE)
    :email: models.CharField(max_length=200, null=True)
    :date_created: models.DateTimeField(auto_now_add=True, null=True)
    :return: the Customer object created with user, name, email all set to name
    """
    return Customer.objects.get_or_create(
        user=user, name=name, email=name
    )


def create_category(name):
    """Utility function to create a Category usable for views tests
    #     options = (
    #         ('breakfast', 'breakfast'),
    #         ('lunch', 'lunch'),
    #         ('dinner', 'dinner'),
    #         ('snacks', 'snacks'),
    #     )
    #     name = models.CharField(max_length=50, choices=options)
    :return: the Category object created with name
    """
    return Category.objects.create(name=name)


def create_user(name, group, is_staff):
    user = User.objects.get(username=name)
    if user:
        return user
    return User.objects.create_user(username=name)


class TestModels(TestCase):
    # Customer
    def test_customer___str__(self):
        # Prepare test
        user = create_user(self._testMethodName, "user", False)
        customer = create_customer(self._testMethodName, user)[0]

        # Run test
        customer_str = str(customer)

        # Evaluate test
        self.assertEqual(customer.name, customer_str)

    # Category
    def test_category___str__(self):
        # Prepare test
        category = create_category(self._testMethodName)

        # Run test
        category_str = str(category)

        # Evaluate test
        self.assertEqual(category.name, category_str)

    # Food item
    def test_fooditem___str__(self):
        # Prepare test
        fooditem = create_fooditem(self._testMethodName)

        # Run test
        fooditem_str = str(fooditem)

        # Evaluate test
        self.assertEqual(fooditem.name, fooditem_str)
