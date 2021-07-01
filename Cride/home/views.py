from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.utils.timezone import now

from django.urls import reverse
from django.http import HttpResponseRedirect
from .forms import LoginForm



# Create your views here.

def login_view(request):

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user:
            login(request,user)
            return redirect("dashboard_home")
        else:
            return render(request,"home_login.html",{"error":"Nombre de usuario o password incorrectos."})

        print(username)
        print(password)

    return render(request,"home_login.html")

def dashboard_home(request):
    return render(request,"home_index.html")



