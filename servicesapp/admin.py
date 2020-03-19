from django.contrib import admin

from .models import Service_object
from .models import Service_picture


class Service_pictureInline(admin.TabularInline):
    model = Service_picture
    exclude = ('title', 'slug',)
    extra = 0

class Service_objectAdmin(admin.ModelAdmin):
	list_display = (
					'object_title',
					'object_desc',
					'object_top',
					)
	
	inlines 	 = [Service_pictureInline]

	exclude = ('object_slug',)

admin.site.register(Service_object, Service_objectAdmin)