from django.urls import path

from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('accounts/login/', views.sign_in, name='accounts.login'),
    path('accounts/register/', views.sign_up, name='accounts.register'),
    path('accounts/logout/', views.loggout, name='accounts.logout'),

    path('books/', views.books_index, name="books.index"),
    path('books/create', views.books_create, name="books.create"),

    path('loans/', views.loans_index, name="loans.index"),
    path('loans/create', views.loans_create, name="loans.create"),
    path('loans/<int:loan_id>back', views.loans_back, name="loans.back"),

    path('loan-users/create', views.loans_user_create, name="loans_user.create"),
]