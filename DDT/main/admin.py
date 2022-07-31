from django.contrib import admin

from .models import Balance, Lender, Borrower

admin.site.register(Balance)
admin.site.register(Lender)
admin.site.register(Borrower)
