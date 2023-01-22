from django.contrib import admin
from authentication import models


class Users(admin.ModelAdmin):
    """
    Настройки отображения, фильтрации и поиска модели:'Todo' на панели администратора
    """

    list_display = (
        # 'id',
        'username',
        'password',
    )
    list_display_links = (
        # 'id',
        'username',
        'password',
    )
    list_editable = (
        # 'title',
    )
    list_filter = (
        # 'id',
        'username',
        'password',
    )
    fieldsets = (
        ('Основное', {'fields': (
            # 'id',
            'username',
            'password',
        )}),
    )
    search_fields = [
        # 'id',
        'username',
        'password',
    ]


admin.site.register(models.Users, Users)
