"""The test of Aggregator News
-----------------------------

Project structure
-----------------
*aggnews/project/app/*
    **tests.py**:
        The test of Aggregator News

About this Module
------------------
The goal of this module is to test the models.
"""

__author__ = "Benoit Lapointe"
__date__ = "2021-03-23"
__copyright__ = "Copyright 2021, labesoft"
__version__ = "1.0.0"

from app.models import Headline
from django.test import TestCase


def create_headline(name):
    """Utility function to create a Headline usable for views tests

    :title: models.CharField(max_length=200, primary_key=True)
    :image: models.URLField(null=True, blank=True)
    :url: models.TextField()
    :created_at: models.DateTimeField(auto_now_add=True, null=True)

    :return: the Headline object created with title, image, url
    """
    return Headline.objects.create(
        title=name, image=name, url=name
    )


class TestModels(TestCase):
    """Testing the models of Aggregator News"""

    def test_headline___str__(self):
        """Test is the str call returns the title"""
        # Prepare test
        headline = create_headline(self._testMethodName)

        # Run test
        headline_str = str(headline)

        # Evaluate test
        self.assertEqual(headline.title, headline_str)
