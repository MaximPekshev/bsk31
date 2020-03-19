from django.contrib import admin
from .models import Rent_object
from .models import Rent_picture


class Rent_pictureInline(admin.TabularInline):
    model = Rent_picture
    exclude = ('title', 'slug',)
    extra = 0

class Rent_objectAdmin(admin.ModelAdmin):
	list_display = (
					'object_title',
					'object_desc',
					'rent_category',
					'object_top',
					)
	
	inlines 	 = [Rent_pictureInline]

	exclude = ('object_slug',)

admin.site.register(Rent_object, Rent_objectAdmin)

