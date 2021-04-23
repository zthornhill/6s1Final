from django.contrib import admin
from .models import Subscription, CustomUser


class SubList(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'start_date', 'end_date')
    list_filter = ('name', 'description', 'price')
    search_fields = ('name', 'price')
    ordering = ['name']

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ["username"]

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Subscription, SubList)

