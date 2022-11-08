from django.db import models


# Create your models here.


class Person(models.Model):
    fullname = models.CharField(
        verbose_name="fullname",
        default="",
        editable=True,
        blank=True,
        max_length=50
    )
    age = models.IntegerField(
        verbose_name="age",
        default=0,
        editable=True,
        blank=True,
    )
    child_fullname = models.CharField(
        verbose_name="child_fullname",
        default="",
        editable=True,
        blank=True,
        max_length=50
    )

    # class Meta:
    #     app_label = 'django_app'
    #     ordering = ('id',)
    #     verbose_name = 'Задача'
    #     verbose_name_plural = 'Задачи'
    #     # db_table


class Child(models.Model):
    fullname = models.CharField(
        verbose_name="fullname",
        default="",
        editable=True,
        blank=True,
        max_length=50
    )
    age = models.IntegerField(
        verbose_name="age",
        default=0,
        editable=True,
        blank=True,
    )
    parent_fullname = models.CharField(
        verbose_name="parent_fullname",
        default="",
        editable=True,
        blank=True,
        max_length=50
    )


class Ice_cream(models.Model):
    title = models.CharField(
        verbose_name="title",
        default="",
        editable=True,
        blank=True,
        max_length=50
    )
    manufacturer = models.CharField(
        verbose_name="manufacturer",
        default="",
        editable=True,
        blank=True,
        max_length=50
    )


class Ice_cream_kiosk(models.Model):
    seller_fullname = models.CharField(
        verbose_name="seller_fullname",
        default="",
        editable=True,
        blank=True,
        max_length=50
    )
    owner = models.CharField(
        verbose_name="owner",
        default="",
        editable=True,
        blank=True,
        max_length=50
    )
    geolocation = models.CharField(
        verbose_name="geolocation",
        default="",
        editable=True,
        blank=True,
        max_length=50
    )
