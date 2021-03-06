# Generated by Django 3.0.4 on 2020-03-18 12:05

from django.db import migrations, models
import django.db.models.deletion
import servicesapp.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service_object',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_title', models.CharField(max_length=150, verbose_name='Наименование')),
                ('object_desc', models.TextField(blank=True, max_length=1024, verbose_name='Описание')),
                ('object_top', models.BooleanField(default=False, verbose_name='Поднять в топ')),
                ('object_slug', models.SlugField(blank=True, max_length=10, verbose_name='Url')),
                ('service_category', models.CharField(choices=[('front-works', 'Фасадные работы'), ('roofing', 'Кровельные работы'), ('electrical', 'Элетромонтаж'), ('metalwork', 'Металлоконструкции'), ('reconstruction', 'Реконструкция зданий'), ('construction', 'Строительство')], default='front-works', max_length=15, verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Услуга',
                'verbose_name_plural': 'Услуги',
            },
        ),
        migrations.CreateModel(
            name='Service_picture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=150, verbose_name='Наименование')),
                ('slug', models.SlugField(blank=True, max_length=10, verbose_name='Url')),
                ('object_image', models.ImageField(blank=True, default=None, null=True, upload_to=servicesapp.models.get_image_name, verbose_name='Изображение 1170х780')),
                ('service_object', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='servicesapp.Service_object', verbose_name='Услуга')),
            ],
            options={
                'verbose_name': 'Картинка',
                'verbose_name_plural': 'Картинки',
            },
        ),
    ]
