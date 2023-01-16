from django.contrib import admin
from django_app import models




class Books(admin.ModelAdmin):
    """
    Настройки отображения, фильтрации и поиска модели:'Todo' на панели администратора
    """

    list_display = (
        'title',
        'description',
        'price',
        # 'date',
        'status',
        'url_img',

    )
    list_display_links = (
        'title',
        'description',
        'price',
        # 'date',
        'status',
        'url_img',
    )
    list_editable = (

    )
    list_filter = (
        'title',
        'description',
        'price',
        # 'date',
        'status',
        'url_img',
    )
    fieldsets = (
        ('Основное', {'fields': (
            'title',
            'description',
            'price',
            # 'date',
            'status',
            'url_img',
        )}),
    )
    search_fields = [
        'title',
        'description',
        'price',
        # 'date',
        'status',
        'url_img',
    ]


admin.site.register(models.Books, Books)