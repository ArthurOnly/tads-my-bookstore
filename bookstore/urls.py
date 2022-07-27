from django.urls import path

from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('auth/sign_in', views.sign_in, name='auth.sign_in'),
    path('auth/sign_up', views.sign_up, name='auth.sign_up'),
]