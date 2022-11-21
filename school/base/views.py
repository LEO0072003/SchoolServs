from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .models import User, Teacher, Student
from .forms import UserCreation
from django.contrib import messages
# Create your views here.


def homePage(request):
    return render(request, 'base/home.html')

def loginPage(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'Not a valid user')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')

    context = {'page': page}
    return render(request, 'base/login_register.html',context)

def logoutPage(request):
    logout(request)
    return redirect('home')

def registerPage(request):
    page = 'register'
    form = UserCreation()
    context = {'form':form, 'page':page}

    if request.method == 'POST':
        # print(request.POST)
        form = UserCreation(request.POST)
        if form.is_valid:
            user = form.save(commit=False)
            user.save()

            # creating student object
            if user.usertype == 's':
                # print('Hi student')
                Student.objects.create(user=user)

            # creating teacher object
            elif user.usertype == 't':
                # print('Hi teacher')
                Teacher.objects.create(user = user)

            #Logging in the created user
            login(request, user)
            return redirect('home')

        else:
            messages.error(request, 'An error occured during registration.')

    return render(request, 'base/login_register.html',context)

