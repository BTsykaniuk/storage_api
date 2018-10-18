from datetime import datetime

from django.contrib import admin
from .models import Product

from utils.admin_filters import UpdateDateFilter, CreateDateFilter


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    fields = ('name', 'description', 'date_added', 'date_updated')
    list_display = ('name', 'date_added', 'date_updated')
    readonly_fields = ('date_added', 'date_updated')

    list_filter = (CreateDateFilter, UpdateDateFilter,)

    def save_model(self, request, obj, form, change):
        if change:
            obj.date_updated = datetime.today().date()
        super().save_model(request, obj, form, change)
