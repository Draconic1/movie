# Generated by Django 4.1.2 on 2022-10-18 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seats',
            name='number',
            field=models.IntegerField(verbose_name='Номер места'),
        ),
        migrations.AlterField(
            model_name='seats',
            name='row',
            field=models.IntegerField(verbose_name='Ряд'),
        ),
    ]