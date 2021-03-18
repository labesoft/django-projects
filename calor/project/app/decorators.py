"""The auth decorators of The Calorie Calculator Web Application
-----------------------------

About this Module
------------------
The goal of this module is provide decorators to manage authentication.
This will take care of all access privileges so that the customer and the
admin cannot access each other’s data. Also, it will make sure that the
logged-in user can’t go to the login/register page, unauthorized users can’t
access any page except login and registration page.
"""

__author__ = "Benoit Lapointe"
__date__ = "2021-03-17"
__copyright__ = "Copyright 2021, labesoft"
__version__ = "1.0.0"

from django.http import HttpResponse
from django.shortcuts import redirect


def unauthorized_user(view_func):
    """Provide a wrapped function to manage authentication

    :param view_func: the current view funtion
    :return: the wrapped authentication function
    """

    def wrapper_func(request, *args, **kwargs):
        """Redirect user to home only if he authenticated successfully

        :param request: the http request from the user
        :return: redirect to home if user is authenticated,
                  otherwise, the current view function
        """
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return view_func(request, *args, **kwargs)

    return wrapper_func


def allowed_users(allowed_roles=()):
    """Provides the decorator function for late call

    :param allowed_roles: roles allowed to view a page
    :return: the authentication logic to be call later
    """

    def decorator(view_func):
        """The decorator with the view function provided

        :param view_func: the view to be rendered
        :return: the wrapped function to be called later
        """
        def wrapper_func(request, *args, **kwargs):
            """The wrapper function which include the authentication logic

            :param request: the http user request
            :param args: additional arguments
            :param kwargs: additional keyword arguments
            :return: the authenticated view if the role is allowed,
                      otherwise, a HTTP refusal response
            """
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse(
                    "<h1>You are not allowed to access this page</h1>")

        return wrapper_func

    return decorator


def admin_only(view_func):
    """A admin only decorator manager

    :param view_func: the view function to display
    :return: the wrapped function to be late called
    """
    def wrapper_func(request, *args, **kwargs):
        """A wrapper function which manage the authentication logic

        :param request: the HTTP user request provided
        :param args: additional arguments
        :param kwargs: additional keywords arguments
        :return: the view function called if user is admin
                  otherwise, redirect to user's page
        """
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name
        if group == 'user':
            return redirect('user_page')
        if group == 'admin':
            return view_func(request, *args, **kwargs)

    return wrapper_func
