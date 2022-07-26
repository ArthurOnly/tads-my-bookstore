from django.urls import path

from . import views

urlpatterns = [
    path('auth/sign_in', views.sign_in, name='auth.sign_in'),
]