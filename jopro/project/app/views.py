"""The views of the Job Portal Web Application
-----------------------------

About this Module
------------------
The goal of this module is to process context information and render the web
pages from html template.
"""

__author__ = "Benoit Lapointe"
__date__ = "2021-03-24"
__copyright__ = "Copyright 2021, labesoft"
__version__ = "1.0.0"

from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

from .forms import *


def home(request):
    """Renders the home page of jopro web site

    :param request: a http request from the site
    :return: the rendered hr-main page, if user is authenticated
            the rendered job-seeker page, otherwise
    """
    if request.user.is_authenticated:
        candidates = Candidate.objects.filter(
            job__company__name=request.user.username
        ).order_by("job__position")
        offers = JobOffer.objects.filter(
            company__name=request.user.username
        ).order_by("position")
        context = {
            'offers': offers,
            'candidates': candidates
        }
        return render(request, 'hr-main.html', context)
    else:
        offers = JobOffer.objects.all()
        context = {
            'offers': offers,
        }
        return render(request, 'job-seeker.html', context)


def site_logout(request):
    """Logout from jopro site and redirects to login page

    :param request: a http request from the site
    :return: the rendered page
    """
    logout(request)
    return redirect('login')


def site_login(request):
    """Login to jopro site and redirect

    :param request: a http request from the site
    :return: the rendered home page, if successful,
            the rendered login page, otherwise
    """
    if request.user.is_authenticated:
        return redirect('home')
    elif request.method == "POST":
        name = request.POST.get('username')
        pwd = request.POST.get('password')
        user = authenticate(request, username=name, password=pwd)
        if user is not None:
            login(request, user)
            return redirect('home')

    # not authenticated, not a post or login is invalid
    return render(request, 'login.html')


def register(request):
    """Registers a new company to jopro site

    :param request: a http request from the site
    :return: the rendered home page, if user is authencitated
            the rendered login page, if user was created on post
            the rendered register page, otherwise
    """
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            curr_user = form.save()
            Company.objects.create(user=curr_user, name=curr_user.username)
            return redirect('login')
    else:
        form = UserCreationForm()

    # Not authenticated, not a POST or form is not valid
    context = {'form': form}
    return render(request, 'register.html', context)


def job_offer(request):
    """Create a new job offer on the jopro site

    :param request: a http request from the site
    :return: the rendered home page, if successful or not authenticated,
            the rendered job-offer page, otherwise
    """
    if request.user.is_authenticated:
        form = JobOfferForm()
        if request.method == 'POST':
            form = JobOfferForm(request.POST)
            if form.is_valid():
                job_offer_model = form.save(commit=False)
                job_offer_model.company = Company.objects.get(
                    name=request.user.username)
                form.save()
                return redirect('home')
        # Not a post or not valid
        context = {'form': form}
        return render(request, 'job-offer.html', context)
    else:
        return redirect('home')


def apply(request):
    """Create a new application to a job

    :param request:
    :return:
    """
    form = ApplyForm()
    if request.method == 'POST':
        form = ApplyForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'apply-job.html', context)
