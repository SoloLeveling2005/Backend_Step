# Generated by Django 4.1.5 on 2023-01-22 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='description',
            field=models.CharField(max_length=300),
        ),
    ]