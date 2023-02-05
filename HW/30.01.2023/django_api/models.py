from django.db import models


class ToDo(models.Model):
    # id, title, description, price, date_add, status
    # id = models.CharField(max_length=)  # TODO это поле есть по-умолчанию (скрыто)
    title = models.CharField(max_length=200)

    class Meta:
        app_label = 'django_api'
        ordering = ('id',)
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
