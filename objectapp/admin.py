from django.contrib import admin
from .models import Build_object
from .models import Picture


class PictureInline(admin.TabularInline):
    model = Picture
    exclude = ('title', 'slug',)
    extra = 0

class Build_objectAdmin(admin.ModelAdmin):
	list_display = (
					'object_date', 
					'object_title',
					'object_top',
					)
	
	inlines 	 = [PictureInline]

	exclude = ('object_slug',)

admin.site.register(Build_object, Build_objectAdmin)


class PictureAdmin(admin.ModelAdmin):
	list_display = (
					'title', 
					'build_object',
					)
	list_filter = (
					'build_object', 
					)
	exclude = ('slug',)

admin.site.register(Picture, PictureAdmin)


