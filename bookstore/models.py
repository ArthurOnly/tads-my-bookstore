from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext as _

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=254)
    editor = models.CharField(max_length=254, null=True)
    volumn = models.CharField(max_length=100, null=True)
    owner = models.ForeignKey(User, verbose_name=_("Owner"), on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def is_in_loan(self):
        return self.loan_set.filter(returned=False).exists()

class LoanUser(models.Model):
    name = models.CharField(_("Name"), max_length=50)
    celphone = models.CharField(_("Celphone"), max_length=50)
    email = models.EmailField(_("Email"), max_length=254)
    responsible = models.ForeignKey(User, verbose_name=_("Responsible"), on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Loan(models.Model):
    from_user = models.ForeignKey(User, verbose_name=_("From user"), on_delete=models.CASCADE)
    to_user = models.ForeignKey(LoanUser, verbose_name=_("To user"), on_delete=models.CASCADE)
    book = models.ForeignKey(Book, verbose_name=_("Book"), on_delete=models.CASCADE)
    initial_date = models.DateField(_("Initial date"), auto_now_add=False)
    end_date = models.DateField(_("Initial date"), null=True)
    returned = models.BooleanField(_("Returned"))