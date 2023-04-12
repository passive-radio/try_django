from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import UserCreateForm

# Create your views here.


def index(request):
    return render(request, "account/top.html")

def login_view(request):
    print(request, request.method)
    if request.method == "GET":
        print("リクエスト・ゲットがきた")
        return render(request, "account/login.html")
    else: 
        print("リクエスト・ポストがきた")
        
    print("request.POST:", dict(request.POST))
    email = request.POST["email"]
    password = request.POST["password"]
    user = authenticate(request, email=email, password=password)

    login(request, user)
    return render(request, "account/top.html")

def logout_view(request):
    logout(request)

    return render(request, "account/top.html")

def signup_view(request):
    if request.method == "GET":
        context = {"form": UserCreateForm}
        return render(request, "account/signup.html", context)
    
    form = UserCreateForm(request.POST)
    if form.is_valid():
        form.save()
        return render(request, "account/top.html")
    else:
        return render(request, "account/signup.html", {"form": form})