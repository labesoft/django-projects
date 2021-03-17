"""The tests of the Discussion Forum Web app
-----------------------------

About this Module
------------------
The goal of this module is to the the models, the forms and the views of the
Django web application.
"""

__author__ = "Benoit Lapointe"
__date__ = "2021-03-16"
__copyright__ = "Copyright 2021, labesoft"
__version__ = "1.0.0"

from django.test import TestCase
from django.urls import reverse

from .models import Forum, Discussion


def create_forum(name):
    """Utility function to create a Forum usable for views tests

    :param name: from models.CharField(max_length=200, default="anonymous")
    :email: from models.CharField(max_length=200, null=True)
    :topic: from models.CharField(max_length=300)
    :desc: from models.CharField(max_length=1000, blank=True)
    :link: from models.SlugField(max_length=100, null=True)
    :return: a Forum object created with all args set to name
    """
    return Forum.objects.create(
        name=name, email=name, topic=name, description=name, link=name
    )


def create_discussion(name, forum):
    """Utility function to create a Discussion usable for views tests

    :param name:
    :param forum:
    :return: a Discussion object created with all args set to name
    """
    return Discussion.objects.create(forum=forum, discuss=name)


class TestModels(TestCase):
    def test_forum___str__(self):
        """Forum string representation"""
        # Prepare test
        forum = create_forum(name=self._testMethodName)

        # Run test
        forum_str = str(forum)

        # Evaluate test
        self.assertEqual(forum.topic, forum_str)

    def test_discussion___str__(self):
        """Discussion string representation"""
        # Prepare test
        forum = create_forum(self._testMethodName)
        discuss = create_discussion(self._testMethodName, forum)

        # Run test
        discussion_str = str(discuss)

        # Evaluate test
        self.assertEqual(discuss.forum.topic, discussion_str)


class TestViews(TestCase):
    def test_home_empty(self):
        """No forums exist"""
        # Run test
        response = self.client.get(reverse('home'))

        # Evaluate test
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['forums'], [])
        self.assertEqual(response.context['count'], 0)
        self.assertQuerysetEqual(response.context['discussions'], [])

    def test_home_forum(self):
        """A forum on the home page"""
        # Prepare test
        forum = create_forum(self._testMethodName)

        # Run test
        response = self.client.get(reverse('home'))

        # Evaluate test
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['forums'], [forum.__repr__()])
        self.assertEqual(response.context['count'], 1)
        self.assertQuerysetEqual(
            response.context['discussions'], ['<QuerySet []>']
        )

    def test_home_discussion(self):
        """Discussion on the home page"""
        # Prepare test
        forum = create_forum(self._testMethodName)
        discussion = create_discussion(self._testMethodName, forum)

        # Run test
        response = self.client.get(reverse('home'))

        # Evaluate test
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(
            response.context['discussions'],
            [f'<QuerySet [{discussion.__repr__()}]>']
        )

    def test_details_empty(self):
        """No forum on details page"""
        # Run test
        response = self.client.get(
            reverse('details', args=(f'{self._testMethodName}', ))
        )

        # Evaluate test
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['forums'], [])
        self.assertEqual(response.context['count'], 0)
        self.assertQuerysetEqual(response.context['discussions'], [])

    def test_details_forum(self):
        """Forum on the details page"""
        # Prepare test
        create_forum(f'{self._testMethodName}1')
        forum = create_forum(f'{self._testMethodName}2')

        # Run test
        response = self.client.get(reverse('details', args=(forum.link, )))

        # Evaluate test
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['forums'], [forum.__repr__()])
        self.assertEqual(response.context['count'], 1)
