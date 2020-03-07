from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from .forms import RegistrationForm



def signup_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            #log the user in
            return redirect('menu:order')
    else:
        form = RegistrationForm()

    return render(request, 'accounts/signup.html', {'form' : form})

def login_view(request):
    print('login active')
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
        #log in the user
            user = form.get_user()
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get("next"))
            else:
             return redirect('menu:order')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form' : form})

def logout_view(request):
    print('logout active')
    # if request.method == 'POST':
    logout(request)
    return redirect('menu:index')

def all_in_one_view(request):
    x =1
    if request.method == 'POST':
            form = RegistrationForm(request.POST)
            form2 = AuthenticationForm(data=request.POST)
            if form.is_valid():
                user = form.save()
                login(request, user)
                #log the user in
                return redirect('menu:order')
            else:
                if form2.is_valid():
                    #log in the user
                    user = form2.get_user()
                    login(request, user)
                    if 'next' in request.POST:
                        return redirect(request.POST.get("next"))
                    else:
                        return redirect('menu:order')
    else:
        form = RegistrationForm()
        form2 = AuthenticationForm()

    return render(request, 'accounts/aio.html', {'form' : form, 'form2' : form2})