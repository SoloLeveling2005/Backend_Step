from django.db import models


class Books(models.Model):
    # id, title, description, price, date_add, status
    # id = models.CharField(max_length=)  # TODO это поле есть по-умолчанию (скрыто)
    # id = models.IntegerField()
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    date_add = models.IntegerField()
    status = models.BooleanField()
    url_img = models.CharField(max_length=70)


    class Meta:
        app_label = 'django_app'
        ordering = ('id',)
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
