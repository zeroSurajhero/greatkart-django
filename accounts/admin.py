from django.contrib import admin
from .models import Account

class AccountAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "username", "email", "date_joined")
    list_display_links = ("email", "first_name", "last_name")
    readonly_fields = ("password",)
    ordering = ("-date_joined",)


admin.site.register(Account, AccountAdmin)
