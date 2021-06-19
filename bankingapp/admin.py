from django.contrib import admin
from bankingapp.models import Customer


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'account_no', 'current_balance')


admin.site.register(Customer, CustomerAdmin)
