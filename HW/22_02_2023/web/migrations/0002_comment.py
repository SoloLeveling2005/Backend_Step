# Generated by Django 4.1.7 on 2023-03-12 05:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=100)),
                ('post_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.post')),
            ],
        ),
    ]
