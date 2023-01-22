from django.db import models




class Tasks(models.Model):
    # id = models.CharField(max_length=)  # TODO это поле есть по-умолчанию (скрыто)
    # user_id = models.PositiveIntegerField(default=1)

    title = models.CharField(max_length=300)
    # title = models.TextField()
    description = models.CharField(max_length=300)

    created = models.DateTimeField()
    update = models.DateTimeField()

    class Meta:
        app_label = 'django_api'
        ordering = ('id',)
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
