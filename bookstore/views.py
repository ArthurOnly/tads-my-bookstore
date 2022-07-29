from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from bookstore.forms import LoanCreateForm, LoanUserCreateForm, LoginForm, RegisterForm, BookCreateForm
from django.contrib.auth.models import User
from django.utils.translation import gettext as _
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Book, Loan, LoanUser

# Create your views here.

def sign_in(request : HttpRequest) -> HttpResponse:
    login_form = LoginForm(request.POST or None)
    
    if request.method == 'POST' and login_form.is_valid():
        user = authenticate(**login_form.cleaned_data)
        if user is not None:
            login(request, user)
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
        return redirect('accounts.login')
    elif request.method == 'POST':
        messages.error(request, _('Verify the data and try again.'))
        
    return render(request, 'auth/sign_up.html', {'register_form': register_form})

@login_required
def loggout(request: HttpRequest) -> HttpResponse:
    print('before')
    logout(request)
    print('after')
    return redirect('accounts.login')

@login_required
def dashboard(request: HttpRequest) -> HttpResponse:
    return redirect('books.index')

@login_required
def books_index(request: HttpRequest) -> HttpResponse:
    books = request.user.book_set.all()
    return render(request, 'books/index.html', {'books' : books})

@login_required
def books_create(request: HttpRequest) -> HttpResponse:
    book_form = BookCreateForm(request.POST or None)

    if request.method == 'POST' and book_form.is_valid():
        book_form.cleaned_data.update({'owner': request.user})
        book = Book.objects.create(**book_form.cleaned_data)
        messages.success(request, _('Success.'))
        return redirect('books.index')
    elif request.method == 'POST':
        messages.error(request, _('Verify the data and try again.'))
        
    return render(request, 'books/create.html', {'book_form' : book_form})

@login_required
def loans_index(request: HttpRequest) -> HttpResponse:
    loans = Loan.objects.filter(from_user=request.user)
    return render(request, 'loans/index.html', {'loans' : loans})

@login_required
def loans_create(request: HttpRequest) -> HttpResponse:
    loan_form = LoanCreateForm(request.POST or None, user=request.user)

    if request.method == 'POST' and loan_form.is_valid():
        loan_form.cleaned_data.update({'from_user': request.user})
        loan = Loan.objects.create(**loan_form.cleaned_data)
        messages.success(request, _('Success.'))
        return redirect('loans.index')
    elif request.method == 'POST':
        messages.error(request, _('Verify the data and try again.'))
        
    return render(request, 'loans/create.html', {'loan_form' : loan_form})

@login_required
def loans_user_create(request: HttpRequest) -> HttpResponse:
    loan_user_form = LoanUserCreateForm(request.POST or None)

    if request.method == 'POST' and loan_user_form.is_valid():
        loan_user_form.cleaned_data.update({'responsible': request.user})
        loan_user = LoanUser.objects.create(**loan_user_form.cleaned_data)
        messages.success(request, _('Success.'))
        return redirect('loans.create')
    elif request.method == 'POST':
        messages.error(request, _('Verify the data and try again.'))
        
    return render(request, 'loan_user/create.html', {'loan_user_form' : loan_user_form})

def loans_back(request: HttpRequest, loan_id: int) -> HttpResponse:
    loan = get_object_or_404(Loan, pk=loan_id)
    loan.returned = True
    loan.save()
    messages.success(request, _('Success.'))
    return redirect('loans.index')