from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password1 = request.POST['password']

        user = auth.authenticate(username=username, password=password1)

        if user is not None:
            auth.login(request, user)
            return redirect("/")

        else:
            messages.info(request, "Invalid credentials")
            return redirect("login")

    else:
        return render(request, "register.html")


def register(request):

    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if (password1 == password2):
            if User.objects.filter(username=username).exists():
                # print("Username already exist")
                messages.info(request, "Username already exist")
                return redirect("register")

            elif User.objects.filter(email=email).exists():
                # print("Email already exist")
                messages.info(request, "Email already exist")
                return redirect("register")

            else:
                user = User.objects.create(username=username, password=password1,
                                           email=email, first_name=first_name, last_name=last_name)
                user.save()
                print("User Created")
                # return redirect("/")
                return redirect("login")

        else:
            # print("user not created")
            messages.info(request, "Password did not match, try again")
            return redirect("register")

        return redirect("/")

    else:
        return render(request, 'register.html')

    # return render(request, 'register.html')
