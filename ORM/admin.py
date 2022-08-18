from django.contrib import admin
from .models import Borrower, Loan

# Register your models here.
admin.site.register(Borrower)
admin.site.register(Loan)