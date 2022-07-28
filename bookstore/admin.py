from django.contrib import admin
from .models import Book, Loan, LoanUser

# Register your models here.

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    pass
@admin.register(Loan)
class LoanAdmin(admin.ModelAdmin):
    pass

@admin.register(LoanUser)
class LoanUserAdmin(admin.ModelAdmin):
    pass