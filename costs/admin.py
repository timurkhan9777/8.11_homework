from django.contrib import admin
from .models import DailyCosts


@admin.register(DailyCosts)
class DailyCostsAdmin(admin.ModelAdmin):
    list_display = ['pk', 'user', 'title', 'description', 'amount', 'date']
    list_editable = ['title', 'description']
    list_display_links = ['pk', 'user']
