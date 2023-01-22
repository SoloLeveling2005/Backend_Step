from django.contrib import admin
from authentication import models


class Users(admin.ModelAdmin):
    """
    Настройки отображения, фильтрации и поиска модели:'Todo' на панели администратора
    """

    list_display = (
        'id',

    )
    list_display_links = (
        'id',
    )
    list_editable = (
        # 'title',
    )
    list_filter = (
        'id',
    )
    fieldsets = (
        ('Основное', {'fields': (
            'id',
        )}),
    )
    search_fields = [
        'id',
    ]


admin.site.register(models.Users, Users)
