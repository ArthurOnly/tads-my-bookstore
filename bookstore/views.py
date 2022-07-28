from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from bookstore.forms import LoanCreateForm, LoanUserCreateForm, LoginForm, RegisterForm, BookCreateForm
from django.contrib.auth.models import User
from django.utils.translation import gettext as _
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from .models import Book, Loan, LoanUser

# Create your views here.

def sign_in(request : HttpRequest) -> HttpResponse:
    login_form = LoginForm(request.POST or None)
    
    if request.method == 'POST' and login_form.is_valid():
        user = authenticate(**login_form.cleaned_data)
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
        return redirect('books.create')
    elif request.method == 'POST':
        messages.error(request, _('Verify the data and try again.'))
        
    return render(request, 'auth/sign_up.html', {'register_form': register_form})

@login_required
def dashboard(request: HttpRequest) -> HttpResponse:
    return render(request, 'dashboard.html')

def books_index(request: HttpRequest) -> HttpResponse:
    books = Book.objects.all()
    return render(request, 'books/index.html', {'books' : books})

def books_create(request: HttpRequest) -> HttpResponse:
    book_form = BookCreateForm(request.POST or None)

    if request.method == 'POST' and book_form.is_valid():
        book_form.cleaned_data.update({'owner': request.user})
        print(book_form.cleaned_data)
        book = Book.objects.create(**book_form.cleaned_data)
        messages.success(request, _('Success.'))
        return redirect('books.index')
    elif request.method == 'POST':
        messages.error(request, _('Verify the data and try again.'))
        
    return render(request, 'books/create.html', {'book_form' : book_form})

def loans_index(request: HttpRequest) -> HttpResponse:
    loans = Loan.objects.all()
    return render(request, 'loans/index.html', {'loans' : loans})

def loans_create(request: HttpRequest) -> HttpResponse:
    loan_form = LoanCreateForm()

    if request.method == 'POST' and loan_form.is_valid():
        loan_form.cleaned_data.update({'owner': request.user})
        book = Book.objects.create(**loan_form.cleaned_data)
        messages.success(request, _('Success.'))
        return redirect('books.index')
    elif request.method == 'POST':
        messages.error(request, _('Verify the data and try again.'))
        
    return render(request, 'loans/create.html', {'loan_form' : loan_form})

def loans_user_create(request: HttpRequest) -> HttpResponse:
    loan_user_form = LoanUserCreateForm(request.POST or None)

    if request.method == 'POST' and loan_user_form.is_valid():
        loan_user = LoanUser.objects.create(**loan_user_form.cleaned_data)
        messages.success(request, _('Success.'))
        return redirect('loans.create')
    elif request.method == 'POST':
        messages.error(request, _('Verify the data and try again.'))
        
    return render(request, 'loan_user/create.html', {'loan_user_form' : loan_user_form})