from datetime import datetime

from django.contrib import admin
from .models import Item

from utils.admin_filters import UpdateDateFilter, CreateDateFilter


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    fields = ('name', 'description', 'seller', 'date_added', 'date_updated')
    list_display = ('name', 'seller', 'date_added', 'date_updated')
    readonly_fields = ('date_added', 'date_updated')

    list_filter = (CreateDateFilter, UpdateDateFilter,)

    def save_model(self, request, obj, form, change):
        if change:
            obj.date_updated = datetime.today().date()
        super().save_model(request, obj, form, change)
