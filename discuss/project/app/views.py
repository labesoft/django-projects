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
from .forms import *


def home(request):
    """Renders the home page that sends all forums to home template.

    :param request: the request received when home loads
    :return: the rendered response
    """
    forums = Forum.objects.all()
    context = generate_card_context(forums)
    return render(request, "home.html", context=context)


def details(request, slug):
    """Renders the details page that sends the selected forum details template

    :param request: the request received when home loads
    :param slug: the link slug to send the response
    :return: the rendered response
    """
    forums = Forum.objects.filter(link=slug)
    context = generate_card_context(forums)
    return render(request, 'details.html', context=context)


def generate_card_context(forums):
    """Generates the context of card views

    Its response is based on the forum list provided and generates the context
    required for the rendering of the html page.

    :param forums: the forums to include in each cards
    :return: the card context of the forum list
    """
    count = forums.count()
    discussions = []
    for i in forums:
        discussions.append(i.discussion_set.all())
    context = {'forums': forums,
               'count': count,
               'discussions': discussions}
    return context


def add_in_forum(request):
    """Creates a new forum through an instance of CreateInForum

    If there is a context it means that the forum could not be generated
    because it was not valid, we then go back to adding the forum so the user
    can correct his answer. Otherwise the forum was created and we go back to
    home page.

    :param request: the POST request received with the forum data
    :return: the rendered response with the context
    """
    context = generate_addin_context(request, CreateInForum)
    if context:
        return render(request, 'addInForum.html', context)
    else:
        return redirect('/')


def add_in_discussion(request):
    """Creates a new discussion through an instance of CreateInDiscussion

    If there is a context it means that the discussion could not be generated
    because it was not valid, we then go back to adding the forum so the user
    can correct his answer. Otherwise the forum was created and we go back to
    home page.

    :param request: the POST request received with the discussion data
    :return: the rendered response with the context
    """
    context = generate_addin_context(request, CreateInDiscussion)
    if context:
        return render(request, 'addInDiscussion.html', context)
    else:
        return redirect('/')


def generate_addin_context(request, create_class):
    """Generates an empty context on successful class creation and save the form

    When it fails, it generates a context to inform the user why the creation
    failed.

    :param request: the post request provided
    :param create_class: the form fields to validate
    :return: an empty context on valid submission,
                otherwise a context with the form
    """
    form = create_class()
    if request.method == 'POST':
        form = create_class(request.POST)
        if form.is_valid():
            form.save()
            return {}
    context = {'form': form}
    return context


