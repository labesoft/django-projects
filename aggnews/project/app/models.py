"""The Models of The News Aggregator Web App
-----------------------------

About this Module
------------------
The goal of this module is to models the news aggregator web app. Our models
will be able to store three things:

- Title of the article
- URL of the origin or source
- URL of the article image

We are using simple model fields for that purpose. Also, the image field can
be blank.
"""

__author__ = "Benoit Lapointe"
__date__ = "2021-03-19"
__copyright__ = "Copyright 2021, labesoft"
__version__ = "1.0.0"

from django.db import models


class Headline(models.Model):
    """Stores the urls and articles in our database"""
    title = models.CharField(max_length=200, primary_key=True)
    image = models.URLField(null=True, blank=True)
    url = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        """The string representation of the object."""
        return self.title
