from django.contrib import admin

# Register your models here.
from web import models

admin.site.register(models.Post)
admin.site.register(models.Like)
admin.site.register(models.Comment)
