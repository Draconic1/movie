# Generated by Django 4.1.2 on 2022-10-31 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_alter_users_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='films',
            name='image',
            field=models.CharField(default='', max_length=255, verbose_name='Изображение'),
        ),
    ]
