from django.contrib import admin

from .models import Driver
from .models import Working_day


class Working_dayInline(admin.TabularInline):
    model = Working_day
    exclude = ('slug', 'debt_of_day')
    extra = 0

class DriverAdmin(admin.ModelAdmin):
	
	list_display = (
					'first_name',
					'second_name',
					'third_name',
					)

	inlines		= [Working_dayInline]

	exclude = ('slug',)

admin.site.register(Driver, DriverAdmin)


class Working_dayAdmin(admin.ModelAdmin):
	list_display = (
					'date',
					'rate',
					'fuel',
					'penalties',
					'cash',
					'cashless',
					)	

	exclude = ('slug', 'debt_of_day',)


admin.site.register(Working_day, Working_dayAdmin)
