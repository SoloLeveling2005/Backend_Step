from django.db import models

class Posts(models.Model):
    # id = models.CharField(max_length=)  # TODO это поле есть по-умолчанию (скрыто)
    user_id = models.PositiveIntegerField(default=1)

    title = models.CharField(max_length=300)
    # title = models.TextField()
    completed = models.BooleanField(default=False)

    # created = models.DateTimeField()
    # update = models.DateTimeField()

    class Meta:
        app_label = 'django_api'
        ordering = ('id',)
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    # def __str__(self):  # TODO <object 1>
    #     return f'{self.id} {self.user_id} {"Выполнено" if self.completed else "Не выполнено"} {self.title[0:50:1]}'