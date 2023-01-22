from django.db import models




class Users(models.Model):
    id = models.CharField(max_length=255)  # TODO это поле есть по-умолчанию (скрыто)

    class Meta:
        app_label = 'authentication'
        ordering = ('id',)
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
