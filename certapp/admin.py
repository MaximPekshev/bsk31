from django.contrib import admin

from .models import Cert_object
from .models import Picture as Cert_picture


class Cert_pictureInline(admin.TabularInline):
    model = Cert_picture
    exclude = ('title', 'slug',)
    extra = 0

class Cert_objectAdmin(admin.ModelAdmin):

	list_display = (
					'object_title',
					)
	
	inlines 	 = [Cert_pictureInline]

	exclude = ('object_slug',)

admin.site.register(Cert_object, Cert_objectAdmin)
