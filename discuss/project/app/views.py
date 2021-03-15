"""The Views of the Discussion Forum Web Application
-----------------------------

About this Module
------------------
The goal of this module is to create the frontend behaviour of The Discussion
Forum.
"""

__author__ = "Benoit Lapointe"
__date__   = "2021-03-15"
__copyright__ = "Copyright 2021, labesoft"
__version__ = "1.0.0"

from django.shortcuts import render, redirect
from .models import *
from .forms import *


def home(request):
    """The home page that takes all forums and discussion objects

    It then passes them to the templates through a dictionary named context.
    This page links to both the other pages and shows all the required
    information to the user with the feature of adding more information in
    any forum.

    :param request: the request received when home loads
    :return: the rendered response with the context
    """
    forums = forum.objects.all()
    count = forums.count()
    discussions = []
    for i in forums:
        discussions.append(i.discussion_set.all())

    context = {'forums': forums,
               'count': count,
               'discussions': discussions}
    return render(request, 'home.html', context)


def details(request, slug):
    forums = [forum.objects.get(link=slug)]
    discussions = [forums[0].discussion_set.all()]
    context = {'forums': forums,
               'count': 1,
               'discussions': discussions}
    return render(request, 'home.html', context)


def addInForum(request):
    """Creates a new forum through an instance of CreateInForum() object

    It was defined in forms.py and also, it takes the filled data through
    request.POST and checks if the data is valid to save it in our database
    and after successfully storing it redirects to the home page otherwise it
    again asks user to fill the correct information

    :param request: the POST request received with the forum data
    :return: the rendered response with the context
    """
    form = CreateInForum()
    if request.method == 'POST':
        form = CreateInForum(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'addInForum.html', context)


def addInDiscussion(request):
    """This is very similar to add in forum, but add new discussions

    The used is then to add opinions to existing forums.

    :param request: the POST request received with the discussion data
    :return: the rendered response with the context
    """
    form = CreateInDiscussion()
    if request.method == 'POST':
        form = CreateInDiscussion(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'addInDiscussion.html', context)
