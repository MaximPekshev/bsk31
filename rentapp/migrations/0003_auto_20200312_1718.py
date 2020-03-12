# Generated by Django 3.0.3 on 2020-03-12 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rentapp', '0002_rent_object_rent_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rent_object',
            name='rent_category',
            field=models.CharField(choices=[('EQ', 'Техника'), ('TL', 'Инструмент')], default='EQ', max_length=2, verbose_name='Категория'),
        ),
    ]
