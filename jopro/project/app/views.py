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
from django.shortcuts import render, redirect

from .forms import *


def home(request):
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
        return render(request, 'Hr.html', context)
    else:
        offers = JobOffer.objects.all()
        context = {
            'offers': offers,
        }
        return render(request, 'Jobseeker.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


def loginUser(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == "POST":
            name = request.POST.get('username')
            pwd = request.POST.get('password')
            user = authenticate(request, username=name, password=pwd)

            if user is not None:
                login(request, user)
                return redirect('home')
        return render(request, 'login.html')


def registerUser(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = UserCreationForm()
        if request.method == 'POST':
            form = UserCreationForm(request.POST)

            if form.is_valid():
                currUser = form.save()
                Company.objects.create(user=currUser, name=currUser.username)
                return redirect('login')
        context = {
            'form': form
        }
        return render(request, 'register.html', context)


def job_offer(request):
    if not request.user.is_authenticated:
        return redirect('home')
    else:
        form = JobOfferForm()
        if request.method == 'POST':
            form = JobOfferForm(request.POST)

            if form.is_valid():
                joboffer = form.save(commit=False)
                joboffer.company = Company.objects.get(name=request.user.username)
                form.save()
                return redirect('home')
        context = {
            'form': form
        }
        return render(request, 'joboffer.html', context)


def applyPage(request):
    form = ApplyForm()
    if request.method == 'POST':
        form = ApplyForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'apply.html', context)
