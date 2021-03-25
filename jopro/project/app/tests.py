"""The tests of the Job Portal Web Application
-----------------------------

About this Module
------------------
The goal of this module is test the models of the jopro Job Portal webapp.
"""

__author__ = "Benoit Lapointe"
__date__   = "2021-03-25"
__copyright__ = "Copyright 2021, labesoft"
__version__ = "1.0.0"

from django.contrib.auth.models import User
from django.test import TestCase

from app.models import Company, JobOffer, Candidate
from django.utils import timezone


def create_company(name):
    """Utility function to create a Company usable for views tests

    :param name: models.CharField(max_length=200, null=True)
    :user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)

    :return: the Company object created with user, name
    """
    return Company.objects.create(
        user=User.objects.create(), name=name
    )


def create__job_offer(name):
    """Utility function to create a JobOffer usable for views tests

    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    position = models.CharField(max_length=200, null=True)
    description = models.CharField(max_length=2000, null=True)
    salary = models.IntegerField(null=True)
    experience = models.IntegerField(null=True)
    location = models.CharField(max_length=2000, null=True)

    :return: the JobOffer object created with user, name
    """
    return JobOffer.objects.create(
        company=create_company(name), position=name, description=name,
        salary=hash(name), experience=hash(name), location=name
    )


def create__candidate(name):
    """Utility function to create a Candidate usable for views tests

    :param name: models.CharField(max_length=200, null=True)
    dob = models.DateField(null=True)
    gender = models.CharField(max_length=200, null=True, choices=category)
    mobile = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    resume = models.FileField(null=True)
    job = models.ForeignKey(JobOffer, on_delete=models.CASCADE)

    :return: the Candidate object created with name, dob, gender, mobile,
    email, resume, job,
    """
    return Candidate.objects.create(
        name=name, dob=timezone.now(), gender=name, mobile=name, email=name,
        resume=name, job=create__job_offer(name)
    )


class TestModels(TestCase):
    def test_company___str__(self):
        """Test Company string representation"""
        # Prepare test
        company = create_company(self._testMethodName)

        # Run test
        company_str = str(company)

        # Evaluate test
        self.assertEqual(company.name, company_str)

    def test_job_offer___str__(self):
        """Test JobOffer string representation"""
        # Prepare test
        job_offer = create__job_offer(self._testMethodName)

        # Run test
        job_offer_str = str(job_offer)

        # Evaluate test
        self.assertEqual(job_offer.position, job_offer_str)

    def test_candidate___str__(self):
        """Test Candidate string representation"""
        # Prepare test
        candidate = create__candidate(self._testMethodName)

        # Run test
        candidate_str = str(candidate)

        # Evaluate test
        self.assertEqual(candidate.name, candidate_str)
