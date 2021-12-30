from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from .models import Account
from django.contrib import messages, auth
from django.contrib.auth import (
                                  authenticate,
                                  logout ,
                                  login
                              )
from django.shortcuts import (
                                  render,
                                  get_object_or_404,
                                  redirect
                              )
from .forms import (
                    RegistrationForm,
                    AccountAuthenticationForm,
                    AccountUpdateform,
                    AccountGeneralForm
                )
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.conf import settings


def login_view(request):
    formLogin = AccountAuthenticationForm(request.POST or None)

    context = {
        "formLogin": formLogin
    }
    user = request.user

    if user.is_authenticated:
        return redirect("index")

    if formLogin.is_valid():
        email = formLogin.cleaned_data["email"]
        password = formLogin.cleaned_data["password"]
        user =  authenticate(email=email, password=password)
        if user:
            login(request, user)
            print("loged in asdas")
            messages.success(request, "You have successfully login.")
            return redirect("index")
        else:
            messages.error("please Correct Below Errors")

    return render(request, "account/login.html", context)


def registration_view(request):
    formRegister = RegistrationForm(request.POST or None)

    context = {
        "formRegister": formRegister,
    }
    user = request.user

    if user.is_authenticated:
        return redirect("currentState")

    if formRegister.is_valid():
        formRegister.save()
        email    = formRegister.cleaned_data.get('email')
        raw_pass = formRegister.cleaned_data.get('password1')
        account = authenticate(email=email, password = raw_pass)
        login(request, account)

        messages.success(request, "Kaydı başarıyla tamamladınız. {}".format(request.user.username))
        return redirect('index')
    else:
        messages.error(request, "Please Correct Below Errors")

    return render(request, "account/registration.html", context)


@login_required(login_url = "accounts:authentication")
def settings(request, id):
    account = get_object_or_404(Account, id = id)
    context = {
        "account": account,
    }

    return render(request, "account/settings.html", context)


def test(request, id):
    print("hey")
    print(id)
    return render(request, "account/settings.html")


def settingsGeneral(request, id):
    account = get_object_or_404(Account, id = id)
    form = AccountGeneralForm(request.POST or None, instance=account)
    context = {
        "account" : account,
        "form" : form
    }

    if form.is_valid():
        new_account = form.save(commit=False)
        new_account.user = request.user
        new_account.save()
        messages.success(request, "Account updated successfully.")
        return redirect(reverse("accounts:accountSettings", kwargs={"id" : id}))

    return render(request, "account/settings.html", context)


@login_required(login_url = "accounts:authentication")
def logout_view(request):
    logout(request)
    messages.success(request, "Logged Out")
    return redirect("accounts:authentication")


@login_required(login_url = "accounts:authentication")
def changePassword(request, id):
    error = ''
    if request.method == "POST":
        username = request.user.username
        email = request.user.email
        password = request.POST.get('password')
        new_password = request.POST.get('new_password')
        re_new_password = request.POST.get('re_new_password')
        #ok = auth.authenticate(username=username, password=password)
        ok = auth.authenticate(email = email, password = password)
        print(request)
        print(username)
        print(password)
        print(ok)
        if ok:
            auth.login(request, ok)
            print("The original account password is correct")
            if new_password:
                print("Password is not empty")
                if new_password == re_new_password:
                    print("The two passwords are the same")
                    request.user.set_password(new_password)
                    request.user.save()
                    #return redirect(reverse('login'))
                    return redirect(reverse("accounts:accountSettings", kwargs={"id" : id}))
                else:
                    error = "The two passwords are inconsistent"

            else:
                error = "password can not be blank"
        else:
            error = "The original account or password is incorrect"

    return render(request, 'account/settings.html', context={"error": error})