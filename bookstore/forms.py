from django.forms import BooleanField, DateField, DateInput, Form, ValidationError, CharField, PasswordInput, EmailField, ModelChoiceField
from django.utils.translation import gettext as _
from django.contrib.auth.models import User

class LoginForm(Form):
    username = CharField(label=_('Username'), max_length=100)
    password = CharField(label=_('Password'), max_length=100, widget=PasswordInput)

class RegisterForm(Form):
    username = CharField(label=_('Username'), max_length=100)
    email = EmailField(label=_('Email'), max_length=100)
    first_name = CharField(label=_('First name'), max_length=100)
    last_name = CharField(label=_('Last name'), max_length=100)
    password = CharField(label=_('Password'), max_length=100, widget=PasswordInput)
    password_confirmation = CharField(label=_('Password confirmation'), max_length=100, widget=PasswordInput)

    def clean_username(self):
        username = self.cleaned_data['username']
        exists = User.objects.filter(username=username)
        if exists:
            raise ValidationError(_('The username is already been taken.'))

        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        exists = User.objects.filter(email=email)
        if exists:
            raise ValidationError(_('The email is already been taken.'))

        return email

class BookCreateForm(Form):
    title = CharField(label=_('Title'), max_length=254)
    editor = CharField(label=_('Editor'), max_length=254)
    volumn = CharField(label=_('Volumn'), max_length=100)

class LoanCreateForm(Form):
    initial_date = DateField(widget=DateInput(format='%d-%m-%Y'), label=_('Initial date'))
    end_date = DateField(widget=DateInput, label=_('End date'))
    returned = BooleanField(label=_('Returned'))

class LoanUserCreateForm(Form):
    name = CharField(label=_('Name'), max_length=100)
    email = EmailField(label=_('Email'), max_length=100)
    celphone = CharField(label=_('Celphone'), max_length=100)