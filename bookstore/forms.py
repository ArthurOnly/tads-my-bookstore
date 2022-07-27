from django.forms import Form, ValidationError, CharField, PasswordInput, EmailField
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