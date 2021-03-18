"""The views of The Calorie Calculator Web Application
-----------------------------

Project structure
-----------------
*calor/project/app/*
    **views.py**:
        The views of The Calorie Calculator Web Application

About this Module
------------------
The goal of this module is to render all view required by the urls and
templates of this web application.
"""

__author__ = "Benoit Lapointe"
__date__ = "2021-03-17"
__copyright__ = "Copyright 2021, labesoft"
__version__ = "1.0.0"

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.shortcuts import render

from .decorators import *
from .filters import FooditemFilter
from .forms import *


@login_required(login_url='login')
@admin_only
def home(request):
    """Render the admin home page with every category and customer possible

    :param request: the HTTP request received from the user for the main page
    :return: the rendered response with all food information available up to
                5 items
    """
    breakfast = Category.objects.filter(name='breakfast')[0].fooditem_set.all()[
                :5]
    lunch = Category.objects.filter(name='lunch')[0].fooditem_set.all()[:5]
    dinner = Category.objects.filter(name='dinner')[0].fooditem_set.all()[:5]
    snacks = Category.objects.filter(name='snacks')[0].fooditem_set.all()[:5]
    customers = Customer.objects.all()
    context = {'breakfast': breakfast,
               'lunch': lunch,
               'dinner': dinner,
               'snacks': snacks,
               'customers': customers,
               }
    return render(request, 'main.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def fooditem(request):
    """Renders all information connected with a food item

    :param request: the HTTP request received from the user for a fooditem page
    :return: the rendered response with all category available for the fooditem
                required by the request
    """
    breakfast = Category.objects.filter(name='breakfast')[0].fooditem_set.all()
    bcnt = breakfast.count()
    lunch = Category.objects.filter(name='lunch')[0].fooditem_set.all()
    lcnt = lunch.count()
    dinner = Category.objects.filter(name='dinner')[0].fooditem_set.all()
    dcnt = dinner.count()
    snacks = Category.objects.filter(name='snacks')[0].fooditem_set.all()
    scnt = snacks.count()
    context = {'breakfast': breakfast,
               'bcnt': bcnt,
               'lcnt': lcnt,
               'scnt': scnt,
               'dcnt': dcnt,
               'lunch': lunch,
               'dinner': dinner,
               'snacks': snacks,
               }
    return render(request, 'fooditem.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def create_fooditem(request):
    """Renders the page with the form to create a food item

    :param request: the HTTP request to create a new food item
    :return: if the creation is success, redirect to home page,
                otherwise stay on the page to correct the form
    """
    form = FooditemForm()
    if request.method == 'POST':
        form = FooditemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'create_fooditem.html', context)


@unauthorized_user
def register_page(request):
    """Renders the page to register a new user

    :param request: the HTTP request received register a new user
    :return: if the user registered, redirect to login page,
                otherwise, stay on the page to correct form
    """
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            group = Group.objects.get(name='user')
            user.groups.add(group)
            email = form.cleaned_data.get('email')
            Customer.objects.create(user=user, name=username, email=email)
            messages.success(request, 'Account created for ' + username)
            return redirect('login')
    context = {'form': form}
    return render(request, 'register.html', context)


@unauthorized_user
def login_page(request):
    """Renders the login page which require both username and password

    :param request: the HTTP request received from the user to login
    :return: if the login is successful redirect to home,
                otherwise, stays on page to correct form
    """
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'username or password is invalid')
    return render(request, 'login.html')


@login_required(login_url='login')
def logout_user(request):
    """Renders the page to logout of the application

    :param request: the HTTP request received from the user to logout
    :return: redirect to login page
    """
    logout(request)
    return redirect('login')


def user_page(request):
    """Renders the user personal page with his food and calorie information

    :param request: the HTTP request received for a user page
    :return: the rendered response with all user's food and calorie information
    """
    user = request.user
    cust = user.customer
    fooditems = Fooditem.objects.filter()
    myfilter = FooditemFilter(request.GET, queryset=fooditems)
    fooditems = myfilter.qs
    total = UserFooditem.objects.all()
    myfooditems = total.filter(customer=cust)
    cnt = myfooditems.count()
    queryset_food = []
    for food in myfooditems:
        queryset_food.append(food.fooditem.all())
    final_food_items = []
    for items in queryset_food:
        for food_items in items:
            final_food_items.append(food_items)
    total_calories = 0
    for foods in final_food_items:
        total_calories += foods.calorie
    calorie_left = 2000 - total_calories
    context = {'calorie_left': calorie_left, 'total_calories': total_calories,
               'cnt': cnt, 'foodlist': final_food_items, 'fooditem': fooditems,
               'myfilter': myfilter}
    return render(request, 'user.html', context)


def add_fooditem(request):
    """Renders food item at the user's page

    :param request: the HTTP request received from the user to add his fooditem
    :return: if the food item is complete, redirect to user page
                otherwise, stays on the form waiting for correction
    """
    user = request.user
    cust = user.customer

    if request.method == "POST":
        form = AddUserFooditem(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    form = AddUserFooditem()
    context = {'form': form}
    return render(request, 'add_user_fooditem.html', context)
