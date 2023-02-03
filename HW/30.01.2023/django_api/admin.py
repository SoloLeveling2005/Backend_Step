from django.contrib import admin
from django_api import models




class ToDo(admin.ModelAdmin):
    """
    Настройки отображения, фильтрации и поиска модели:'Todo' на панели администратора
    """

    list_display = (
        'title',
    )
    list_display_links = (
        'title',
    )
    list_editable = (

    )
    list_filter = (
        'title',
    )
    fieldsets = (
        ('Основное', {'fields': (
            'title',
        )}),
    )
    search_fields = [
        'title',
    ]


admin.site.register(models.ToDo, ToDo)