from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.db.utils import IntegrityError
from django.contrib.auth import authenticate, login, logout
from carapp.models import *


def show_registration(request):
    context = {}

    if request.method == "POST":
        login = request.POST.get("login")
        password = request.POST.get("password")
        password_confirm = request.POST.get("password_confirm")
        
        context["login"] = login
        context["password"] = password
        context["password_confirm"] = password_confirm

        if password == password_confirm:
            try:
                User.objects.create_user(username = login, password = password)
                return redirect('car')

            except IntegrityError:
                context['error'] = 'Користувач вже існує' 
        else:
            context["error"] = "Паролі не спiвпадають"
            
    return render(request, 'reg_form.html', context)

def show_login(request):
    context = {}

    if request.method == 'POST':

        login_user = request.POST.get("login")
        password = request.POST.get("password")
        user = authenticate(request, username = login_user, password = password)

        if user != None:

            login(request, user)
            return redirect('car')
        else:
            context['error'] = 'Логін або пароль невірні'
    return render(request, 'log_form.html', context)
            
def show_car(request):
    if request.user.is_authenticated:
        context = {
            "cars":Car.objects.all(),
            "comments":Comment.objects.all()
            }
        if request.method == "POST":
            text = request.POST.get("content")
            Comment.objects.create(author = request.user.username, text = text)
        return render(request, 'car.html', context)
    else:
        return redirect('log_form')