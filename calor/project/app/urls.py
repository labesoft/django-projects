"""The url mapping of The Calorie Calculator Web App
-----------------------------

Project structure
-----------------
*calor/project/app/*
    **urls.py**:
        The url mapping of The Calorie Calculator Web App

About this Module
------------------
The goal of this module is contains all the urls patterns of The Calorie
Calculator Web Application.
"""

__author__ = "Benoit Lapointe"
__date__ = "2021-03-17"
__copyright__ = "Copyright 2021, labesoft"
__version__ = "1.0.0"

from django.contrib.auth import views as auth_views
from django.urls import path

from app import views

urlpatterns = [
    path('', views.home, name='home'),
    path('user/', views.user_page, name='user_page'),  # user_page
    path('product/', views.fooditem, name='fooditem'),
    path('create_fooditem/', views.create_fooditem, name='create_fooditem'),
    path('register/', views.register_page, name='register'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('add_fooditem/', views.add_fooditem, name='add_fooditem'),
    path(
        'reset_password/',
        auth_views.PasswordResetView.as_view(),
        name="reset_password"
    ),
    path(
        'reset_password_sent/',
        auth_views.PasswordResetDoneView.as_view(),
        name="password_reset_done"
    ),
    path(
        'reset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(),
        name="password_reset_confirm"
    ),
    path(
        'reset_password_complete/',
        auth_views.PasswordResetCompleteView.as_view(),
        name="password_reset_complete"
    ),
]
