from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate

from .forms import SignUpForm
# Create your views here.


def home(request):
    return render(request, 'home.html')


def signup(request):
    context = {}
    if request.POST:
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
        else:
            context['sign_up_form'] = form
    else:
        form = SignUpForm()
        context['sign_up_form'] = form
    return render(request, 'signup.html', context)

