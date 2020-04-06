from django.contrib import admin

from simple_history.admin import SimpleHistoryAdmin

from .models import Driver
from .models import Working_day
from .models import Cashbox


class Working_dayInline(admin.TabularInline):
    model = Working_day
    exclude = ('slug', 'debt_of_day')
    extra = 0

class DriverAdmin(SimpleHistoryAdmin, admin.ModelAdmin):
	
	list_display = (
					'first_name',
					'second_name',
					'third_name',
					)

	inlines		= [Working_dayInline]

	exclude = ('slug',)

admin.site.register(Driver, DriverAdmin)


class Working_dayAdmin(SimpleHistoryAdmin, admin.ModelAdmin):
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


class CashboxAdmin(SimpleHistoryAdmin, admin.ModelAdmin):

	list_display = (
					'date', 
					'cash',
					'cash_card',
					)

	exclude = ('slug',)

admin.site.register(Cashbox, CashboxAdmin)
