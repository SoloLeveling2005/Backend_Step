from django.contrib import admin
from django_api import models


class ToDo(admin.ModelAdmin):
    """
    Настройки отображения, фильтрации и поиска модели:'Todo' на панели администратора
    """

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
            'id',
            'title',
        )}),
    )
    search_fields = [
        'id',
        'title',
    ]


admin.site.register(models.ToDo, ToDo)


class Posts(admin.ModelAdmin):
    """
    Настройки отображения, фильтрации и поиска модели:'Todo' на панели администратора
    """

    list_display = (
        'id',
        'title',
        'description',
        'created_at'
    )
    list_display_links = (
        'id',
        'title',
        'description',
        'created_at'
    )
    list_editable = (

    )
    list_filter = (
        'id',
        'title',
        'description',
        'created_at'
    )
    fieldsets = (
        ('Основное', {'fields': (
            'id',
            'title',
            'description',
            'created_at'
        )}),
    )
    search_fields = [
        'id',
        'title',
        'description',
        'created_at'
    ]


admin.site.register(models.Posts, Posts)
