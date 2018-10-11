from django.contrib import admin
from .models import Product

from utils.admin_filters import UpdateTodayFilter, CreateDateFilter


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    fields = ('name', 'description', 'date_added', 'date_updated')
    list_display = ('name', 'date_added', 'date_updated')
    readonly_fields = ('date_added', 'date_updated')

    list_filter = (CreateDateFilter, UpdateTodayFilter,)
