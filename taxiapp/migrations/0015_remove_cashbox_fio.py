# Generated by Django 3.0.4 on 2020-03-27 09:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('taxiapp', '0014_auto_20200327_1042'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cashbox',
            name='fio',
        ),
    ]
