from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User


# Create your views here.
def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)

        if user is None:
            return render(
                request,
                "account/login.html",
                {"error": "username or password is incorrect !"},
            )
        login(request, user)
        return redirect("home")
    return render(request, "account/login.html")


def register_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        firstname = request.POST["firstname"]
        lastname = request.POST["lastname"]
        password = request.POST["password"]
        repassword = request.POST["repassword"]

        if password == repassword:
            if User.objects.filter(username=username).exists():
                return render(request,"account/register.html",
                    {
                        "error": "username is exsist",
                        "username": username,
                        "email": email,
                        "firstname": firstname,
                        "lastname": lastname,
                    }
                )
            else:
                if User.objects.filter(email=email).exists():
                    return render(request,"account/register.html",
                        {
                            "error": "username is exsist",
                            "username": username,
                            "email": email,
                            "firstname": firstname,
                            "lastname": lastname,
                        }
                    )
                else:
                    user = User.objects.create_user(
                        username=username,
                        email=email,
                        first_name=firstname,
                        last_name=lastname,
                        password=password,
                    )
                    user.save()
                    return redirect("account:login")
        else:
            return render(request,"account/register.html",
            {
                "error": "password isn't same !",
                "username": username,
                "email": email,
                "firstname": firstname,
                "lastname": lastname,
            })
    return render(request, "account/register.html")


def logout_view(request):
    logout(request)
    return redirect("home")


def dashboard_view(request):
    return render(request, "account/dashboard.html")
