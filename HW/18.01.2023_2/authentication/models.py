from django.db import models




class Users(models.Model):
    # id = models.CharField(max_length=255,primary_key=True)  # TODO это поле есть по-умолчанию (скрыто)
    username = models.CharField(max_length=300)
    password = models.CharField(max_length=300)


    class Meta:
        app_label = 'authentication'
        ordering = ('id',)
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
