from multiprocessing import context
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.core.paginator import Paginator
import fooddonation
from .forms import SignUpForm, LoginForm
from django.contrib.auth import authenticate, login
from django.core.mail import send_mail
from django.http import HttpResponse
from django.conf import settings
from .models import *
from django.contrib import messages
import datetime
from django.core.paginator import Paginator
from django.contrib.auth import logout,login
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
# Create your views here.


#register new user
def register(request):
    msg = None
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            userId = form.cleaned_data.get('userId')
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            email = form.cleaned_data.get('email')
            msg = 'user created'
            messages.success(request,'Registered Sucessfully.....')
            return redirect('register')

        else:
            msg = 'form is not valid'
    else:
        form = SignUpForm()
    return render(request,'superadmin/register.html', {'form': form, 'msg': msg})


#login user

def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_superadmin:
                login(request, user)
                return redirect('superadmin')
            elif user is not None and user.is_admin:
                login(request, user)
                return redirect('adminpage')
            elif user is not None and user.is_orphanage:
                login(request, user)
                return redirect('orphanage')
            elif user is not None and user.is_restaurant:
                login(request, user)
                return redirect('restaurant')
            elif user is not None and user.is_people:
                login(request, user)
                return redirect('people')
            else:
                msg= 'invalid credentials'
        else:
            msg = 'error validating form'
    return render(request, 'login/login.html', {'form': form, 'msg': msg})

#logout user
def logout_view(request):
    logout(request)
    return redirect('/login')

#orphanage entry page
@login_required(login_url='login')
def orphanage(request):
    if request.user.is_authenticated:
        if request.user.is_authenticated:
            user=User.objects.all()
            username=request.user
            donate=Orphanage.objects.all()
            p=Paginator(User.objects.all(), 10)
            page=request.GET.get('page')
            users=p.get_page(page)
        return render(request, 'orphanage/orphanage.html',{"user": user, "users":users, "donate":donate})

    else:
        return render(request, 'login/login.html', {})

#superadmin entry page
@login_required(login_url='login')
def superadmin(request):
    if request.user.is_authenticated:
        if request.user.is_authenticated:
            user=User.objects.all()
            p=Paginator(User.objects.all(), 10)
            page=request.GET.get('page')
            users=p.get_page(page)
        return render(request, 'superadmin/superadmin.html',{"user": user, "users":users})

    else:
        return render(request, 'login/login.html', {})

#admin entry page
@login_required(login_url='login')
def adminpage(request):
    if request.user.is_authenticated:
        if request.user.is_authenticated:
            user=User.objects.all()
            donate=Admin.objects.all()
            p=Paginator(User.objects.all(), 10)
            page=request.GET.get('page')
            users=p.get_page(page)
        return render(request, 'admin/admin.html',{"user": user, "users":users})

    else:
        return render(request, 'login/login.html', {})

#restaurant entry page
@login_required(login_url='login')
def restaurant(request):
    if request.user.is_authenticated:
        if request.user.is_authenticated:
            user=User.objects.all()
            username=request.user
            donate=Restaurant.objects.all()
            p=Paginator(User.objects.all(), 10)
            page=request.GET.get('page')
            users=p.get_page(page)
        return render(request, 'restaurant/restaurant.html',{"user": user, "users":users, "donate":donate})

    else:
        return render(request, 'login/login.html', {})

#people entry page
@login_required(login_url='login')
def people(request):
    if request.user.is_authenticated:
        if request.user.is_authenticated:
            user=User.objects.all()
            donate=People.objects.all()
            p=Paginator(User.objects.all(), 10)
            page=request.GET.get('page')
            users=p.get_page(page)
        return render(request, 'people/people.html',{"user": user, "users":users})

    else:
        return render(request, 'login/login.html', {})


#add restaurant
@login_required(login_url='login')
def addrestaurant(request):
    if request.user.is_authenticated:
        if request.method == 'POST':

            username=request.user
            restaurantMobileNo=request.POST["restaurantMobileNo"]
            restaurantMail=request.POST["restaurantMail"]
            available_date=request.POST["available_date"]
            restaurantLocation=request.POST["restaurantLocation"]
            restaurantFoodDescription=request.POST["restaurantFoodDescription"]
            restaurantQuantity=request.POST["restaurantQuantity"]
            


            donate= Restaurant(username=username,restaurantMobileNo=restaurantMobileNo,restaurantMail=restaurantMail,available_date=available_date,
            restaurantLocation=restaurantLocation,restaurantFoodDescription=restaurantFoodDescription,restaurantQuantity=restaurantQuantity)
            donate.save()
            messages.success(request,'restaurant added...')


        return render(request, 'restaurant/addrestaurant.html', {})
    else:
        return render(request, 'login/login.html', {})

#add orphanage
@login_required(login_url='login')
def addorphanage(request):
    if request.user.is_authenticated:
        if request.method == 'POST':

            username=request.user
            orphanageMobileNo=request.POST["orphanageMobileNo"]
            orphanageMail=request.POST["orphanageMail"]
            orphavailable_date=request.POST["orphavailable_date"]
            orphanageLocation=request.POST["orphanageLocation"]
            orphanageDescription=request.POST["orphanageDescription"]
            orphanageQuantity=request.POST["orphanageQuantity"]
            


            donate= Orphanage(username=username,orphanageMobileNo=orphanageMobileNo,orphanageMail=orphanageMail,orphavailable_date=orphavailable_date,
            orphanageLocation=orphanageLocation,orphanageDescription=orphanageDescription,orphanageQuantity=orphanageQuantity)
            donate.save()
            messages.success(request,'Orphanage added...')


        return render(request, 'orphanage/addorphanage.html', {})
    else:
        return render(request, 'login/login.html', {})
