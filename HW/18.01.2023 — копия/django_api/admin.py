from django.contrib import admin
from django_api import models


class Tasks(admin.ModelAdmin):
    """
    Настройки отображения, фильтрации и поиска модели:'Todo' на панели администратора
    """

    list_display = (
        'title',
        'description',
        'created',
        'update',
    )
    list_display_links = (
        'title',
        'description',
        'created',
        'update',
    )
    list_editable = (
        # 'title',
    )
    list_filter = (
        'title',
        'description',
        'created',
        'update',
    )
    fieldsets = (
        ('Основное', {'fields': (
            'title',
            'description',
            'created',
            'update',
        )}),
    )
    search_fields = [
        'title',
        'description',
        'created',
        'update',
    ]


admin.site.register(models.Tasks, Tasks)