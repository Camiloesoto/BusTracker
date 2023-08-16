from django.shortcuts import render

# Create your views here.

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.shortcuts import redirect
from django.db import IntegrityError
from django.contrib.auth.forms import AuthenticationForm


def signupaccount(request):
    return render(request, 'signupaccount.html',

                  {'form': UserCreationForm})


def signupaccount(request):
    if request.method == 'GET':

        return render(request, 'signupaccount.html',

                      {'form': UserCreationForm})

    else:

        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(

                request.POST['username'],

                password=request.POST['password1'])

            user.save()

            login(request, user)

            return redirect('home')


def signupaccount(request):
    if request.method == 'GET':
        return render(request, 'signupaccount.html', {'form': UserCreationForm})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    request.POST['username'],
                    password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('home')
            except IntegrityError:
                return render(request,
                              'signupaccount.html',
                              {'form': UserCreationForm, 'error': 'Username already taken. Choose new username.'})
        else:
            return render(request, 'signupaccount.html', {'form': UserCreationForm, 'error': 'Passwords do not match'})


def loginaccount(request):
    if request.method == 'GET':
        return render(request, 'loginaccount.html', {'form': AuthenticationForm})

    else:

        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])

        if user is None:
            return render(request, 'loginaccount.html', {'form': AuthenticationForm(), 'error': 'username and password do not match'})

        else:
            login(request, user)
            return redirect('home')


def home(request):
    return render(request, 'home.html')