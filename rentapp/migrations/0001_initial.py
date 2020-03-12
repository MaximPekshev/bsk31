# Generated by Django 3.0.3 on 2020-03-12 10:18

from django.db import migrations, models
import django.db.models.deletion
import rentapp.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rent_object',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_title', models.CharField(max_length=150, verbose_name='Наименование')),
                ('object_desc', models.TextField(blank=True, max_length=1024, verbose_name='Описание')),
                ('object_top', models.BooleanField(default=False, verbose_name='Поднять в топ')),
                ('object_slug', models.SlugField(blank=True, max_length=10, verbose_name='Url')),
            ],
            options={
                'verbose_name': 'Объект аренды',
                'verbose_name_plural': 'Объекты аренды',
            },
        ),
        migrations.CreateModel(
            name='Rent_picture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=150, verbose_name='Наименование')),
                ('slug', models.SlugField(blank=True, max_length=10, verbose_name='Url')),
                ('object_image', models.ImageField(blank=True, default=None, null=True, upload_to=rentapp.models.get_image_name, verbose_name='Изображение 1170х780')),
                ('rent_object', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rentapp.Rent_object', verbose_name='Объект аренды')),
            ],
            options={
                'verbose_name': 'Картинка',
                'verbose_name_plural': 'Картинки',
            },
        ),
    ]
