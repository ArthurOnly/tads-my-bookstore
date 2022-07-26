from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.

def sign_in(request : HttpRequest) -> HttpResponse:
    return 