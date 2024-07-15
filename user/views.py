from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import HttpResponse, redirect, render

from user.forms import LoginForm, RegisterForm


# Create your views here.
def user_page(request):
    return HttpResponse("hello,world.User page")


def login_view(request):
    context = {}
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            # username = request.POST['login']
            # password = request.POST['password']
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return redirect('/user/')

        context['error'] = 'Invalid Username or Password'
    context['form'] = LoginForm()

    return render(request, 'login.html', context=context)


def logout_view(request):
    logout(request)
    return redirect('/login/')


def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
        # username = request.POST['username']
        # password = request.POST['password']
        # email = request.POST['email']
        # first_name = request.POST['fname']
        # last_name = request.POST['lname']
            user = User.objects.create_user(username=form.cleaned_data['username'],
                                            email=form.cleaned_data['email'],
                                            password=form.cleaned_data['password'],
                                            first_name=form.cleaned_data['first_name'],
                                            last_name=form.cleaned_data['last_name'])
            user.save()
            return redirect('/login/')
    else:
        return render(request, 'register.html', context={'form': RegisterForm()})

@login_required
def user_page(request):
    return render( request, 'user_page.html', context={"username": request.user.username, "email": request.user.email})
