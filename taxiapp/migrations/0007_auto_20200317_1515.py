# Generated by Django 3.0.3 on 2020-03-17 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taxiapp', '0006_auto_20200317_1257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver',
            name='friday',
            field=models.BooleanField(verbose_name='Пятница'),
        ),
        migrations.AlterField(
            model_name='driver',
            name='monday',
            field=models.BooleanField(verbose_name='Понедельник'),
        ),
        migrations.AlterField(
            model_name='driver',
            name='saturday',
            field=models.BooleanField(verbose_name='Суббота'),
        ),
        migrations.AlterField(
            model_name='driver',
            name='sunday',
            field=models.BooleanField(verbose_name='Воскресенье'),
        ),
        migrations.AlterField(
            model_name='driver',
            name='thursday',
            field=models.BooleanField(verbose_name='Четверг'),
        ),
        migrations.AlterField(
            model_name='driver',
            name='tuesday',
            field=models.BooleanField(verbose_name='Вторник'),
        ),
        migrations.AlterField(
            model_name='driver',
            name='wednesday',
            field=models.BooleanField(verbose_name='Среда'),
        ),
    ]