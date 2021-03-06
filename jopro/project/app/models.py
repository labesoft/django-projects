"""The models of the Job Portal Web Application
-----------------------------

About this Module
------------------
The goal of this module is to model the companies and the canditates of the
Job Portal web site.
"""

__author__ = "Benoit Lapointe"
__date__ = "2021-03-24"
__copyright__ = "Copyright 2021, labesoft"
__version__ = "1.0.0"

from django.contrib.auth.models import User
from django.db import models


class Company(models.Model):
    """The company offering a job"""
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        """The string representation of a company by its name"""
        return self.name


class JobOffer(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    position = models.CharField(max_length=200, null=True)
    description = models.CharField(max_length=2000, null=True)
    salary = models.IntegerField(null=True)
    experience = models.IntegerField(null=True)
    location = models.CharField(max_length=2000, null=True)

    def __str__(self):
        """The string representation of a company by its name"""
        return self.position


class Candidate(models.Model):
    """The person seeking for a job"""
    category = (
        ('Male', 'male'),
        ('Female', 'female'),
        ('Other', 'other'),
    )

    name = models.CharField(max_length=200, null=True)
    dob = models.DateField(null=True)
    gender = models.CharField(max_length=200, null=True, choices=category)
    mobile = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    resume = models.FileField(null=True)
    job = models.ForeignKey(JobOffer, on_delete=models.CASCADE)

    def __str__(self):
        """The string representation of a candidate by his name"""
        return self.name
