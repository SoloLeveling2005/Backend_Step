from django.contrib import admin
from app import models


class Products_category(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
    )
    list_display_links = (
        'id',
        'title',
    )
    list_editable = (

    )
    list_filter = (
        'id',
        'title',
    )
    fieldsets = (
        ('Основное', {'fields': (
            'title',
        )}),
    )
    search_fields = [
        'id',
        'title',
    ]


admin.site.register(models.Products_category, Products_category)


class Products(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'count',
        'price',
        'category'
    )
    list_display_links = (
        'id',
        'title',
        'count',
        'price',
        'category'
    )
    list_editable = (

    )
    list_filter = (
        'id',
        'title',
        'count',
        'price',
        'category'
    )
    fieldsets = (
        ('Основное', {'fields': (
            'title',
            'count',
            'price',
            'category'
        )}),
    )
    search_fields = [
        'id',
        'title',
        'count',
        'price',
        'category'
    ]


admin.site.register(models.Products, Products)
