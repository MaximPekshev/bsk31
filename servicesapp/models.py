from django.db import models

import uuid

def get_uuid():
	return str(uuid.uuid4().fields[0])


class Service_object(models.Model):

	object_title 	= models.CharField(max_length = 150, verbose_name='Наименование')
	object_desc 	= models.TextField(max_length=1024, verbose_name='Описание', blank=True)
	object_top 		= models.BooleanField(verbose_name='Поднять в топ', default=False)

	object_slug 	= models.SlugField(max_length=10, verbose_name='Url', blank=True, db_index=True)

	def __str__(self):

		return self.object_title

	def save(self, *args, **kwargs):

		if self.object_slug == "":
			self.object_slug = get_uuid()


		super(Service_object, self).save(*args, **kwargs)

	class Meta:
		verbose_name = 'Услуга'
		verbose_name_plural = 'Услуги'


def get_image_name(instance, filename):
		
	new_name = ('%s' + ('.') + filename.split('.')[-1]) % instance.slug
	return new_name

class Service_picture(models.Model):

	title 					= models.CharField(max_length=150, verbose_name='Наименование', blank=True)
	slug 					= models.SlugField(max_length=10, verbose_name='Url', blank=True, db_index=True)
	service_object 			= models.ForeignKey('Service_object', verbose_name='Услуга', on_delete=models.CASCADE)

	object_image			= models.ImageField(upload_to=get_image_name, verbose_name='Изображение 1170х780', default=None, null=True, blank=True)

	def __str__(self):
		
		return self.slug


	def save(self, *args, **kwargs):
		
		if self.slug == "":
			self.slug = get_uuid()
			self.title = self.slug

		super(Service_picture, self).save(*args, **kwargs)


	class Meta:
		
		verbose_name = 'Картинка'
		verbose_name_plural = 'Картинки'
