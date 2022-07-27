from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from bookstore.forms import LoginForm, RegisterForm
from django.contrib.auth.models import User
from django.utils.translation import gettext as _
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.

def sign_in(request : HttpRequest) -> HttpResponse:
    login_form = LoginForm(request.POST or None)

    if request.method == 'POST' and login_form.is_valid():
        user = authenticate(**login_form.cleaned_data)
        print(login_form.cleaned_data)
        if user is not None:
            return redirect('dashboard')
        else:
            messages.error(request, 'Verifique suas credenciais.')

    return render(request, 'auth/sign_in.html', {'login_form': login_form})

def sign_up(request : HttpRequest) -> HttpResponse:
    register_form = RegisterForm(request.POST or None)

    if request.method == 'POST' and register_form.is_valid():
        register_form.cleaned_data.pop('password_confirmation')
        user = User.objects.create(**register_form.cleaned_data)
        user.set_password(register_form.cleaned_data['password'])
        user.save()
        messages.success(request, _('Success.'))
        return redirect('auth.sign_in')
    elif request.method == 'POST':
        messages.error(request, _('Verify the data and try again.'))
        
    return render(request, 'auth/sign_up.html', {'register_form': register_form})

@login_required
def dashboard(request: HttpRequest) -> HttpResponse:
    return render(request, 'dashboard.html')