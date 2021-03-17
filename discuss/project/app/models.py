"""The Models of the Discussion Forum Web Application
-----------------------------

About this Module
------------------
The goal of this module is model a discussion forum. It turns key concepts of a
forum into its data representation. This uses the default django data API in
SQLite.

We are using Django inbuilt database SQLite so we do not need to add anything to
our settings.py file. If we change our mind we should change your database
settings in settings.py file.
"""

__author__ = "Benoit Lapointe"
__date__ = "2021-03-15"
__copyright__ = "Copyright 2021, labesoft"
__version__ = "1.0.0"

from django.db import models
from django.utils.text import slugify


class Forum(models.Model):
    """The class Forum define the fields we want here

    Usually Django fields are mandatory, to change this default behavior of
    Django, we add the specific field ‘null=True’ as seen.
    """
    name = models.CharField(max_length=200, default="anonymous")
    email = models.CharField(max_length=200, null=True)
    topic = models.CharField(max_length=300)
    description = models.CharField(max_length=1000, blank=True)
    link = models.SlugField(max_length=100, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def save(self, *args, **kwargs):
        self.link = slugify(self.link)
        super(Forum, self).save(*args, **kwargs)

    def __str__(self):
        """This will return the string representation of the object.

        This uses simple Django concepts.
        """
        return str(self.topic)


class Discussion(models.Model):
    """The child of forum that stores views from different users.

    It has two fields:

    - The forum which is a foreign key (Provide a many-to-one relation by
       adding a column to the local model to hold the remote value). It helps
       in maintaining a record of which opinion belongs to which forum.
    - Discuss – It actually stores the opinion
    """
    forum = models.ForeignKey(Forum, blank=True, on_delete=models.CASCADE)
    discuss = models.CharField(max_length=1000)

    def __str__(self):
        """This will return the string representation of the object.

        This uses simple Django concepts.
        """
        return str(self.forum)
