from django.urls import path

from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('accounts/login/', views.sign_in, name='accounts.login'),
    path('accounts/register/', views.sign_up, name='accounts.register'),

    path('books/', views.books_index, name="books.index"),
    path('books/create', views.books_create, name="books.create")
]