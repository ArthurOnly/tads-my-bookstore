from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.contrib import messages
from bookstore.forms import LoginForm

# Create your views here.

def sign_in(request : HttpRequest) -> HttpResponse:
    form = LoginForm(request.POST or None)

    if request.method == 'POST':
        messages.error(request, 'Verifique suas credenciais.')
    return render(request, 'auth/sign_in.html', {'form': form})