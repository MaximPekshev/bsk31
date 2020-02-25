import datetime
from decimal import Decimal
from django.shortcuts import render, redirect
from .forms import WorkingDayForm
from taxiapp.models import Driver
from taxiapp.models import Working_day



def working_day_add(request, driver_slug):

	driver = Driver.objects.get(slug=driver_slug)

	if request.method == 'POST':

		day_form = WorkingDayForm(request.POST)


		if day_form.is_valid():

			if day_form.cleaned_data['input_date']:
				date = day_form.cleaned_data['input_date']
			else:
				date = datetime.datetime.today()

			if day_form.cleaned_data['input_rate']:
				rate = float(day_form.cleaned_data['input_rate'].replace(',','.'))
			else:
				rate = 0

			if day_form.cleaned_data['input_fuel']:
				fuel = float(day_form.cleaned_data['input_fuel'].replace(',','.'))
			else:
				fuel = 0

			if day_form.cleaned_data['input_penalties']:
				penalties = float(day_form.cleaned_data['input_penalties'].replace(',','.'))
			else:
				penalties = 0	
						
			if day_form.cleaned_data['input_cash']:
				cash = float(day_form.cleaned_data['input_cash'].replace(',','.'))
			else:
				cash = 0

			if day_form.cleaned_data['input_cashless']:
				cashless = float(day_form.cleaned_data['input_cashless'].replace(',','.'))
			else:
				cashless = 0	
			
			new_working_day = Working_day(
				driver=driver,
				date=date,
				rate=rate,
				fuel=fuel,
				penalties=penalties,
				cash=cash,
				cashless=cashless,
				)

			new_working_day.save()

			current_path = request.META['HTTP_REFERER']
			return redirect(current_path)
	else:

		current_path = request.META['HTTP_REFERER']
		return redirect(current_path)	


def working_day_edit(request, day_slug):

	working_day = Working_day.objects.get(slug=day_slug)

	if request.method == 'POST':

		day_form = WorkingDayForm(request.POST)

		if day_form.is_valid():

			if day_form.cleaned_data['input_rate']:
				working_day.rate = float(day_form.cleaned_data['input_rate'].replace(',','.'))
			else:
				working_day.rate = 0

			if day_form.cleaned_data['input_fuel']:
				working_day.fuel = float(day_form.cleaned_data['input_fuel'].replace(',','.'))
			else:
				working_day.fuel = 0

			if day_form.cleaned_data['input_penalties']:
				working_day.penalties = float(day_form.cleaned_data['input_penalties'].replace(',','.'))
			else:
				working_day.penalties = 0	
						
			if day_form.cleaned_data['input_cash']:
				working_day.cash = float(day_form.cleaned_data['input_cash'].replace(',','.'))
			else:
				working_day.cash = 0

			if day_form.cleaned_data['input_cashless']:
				working_day.cashless = float(day_form.cleaned_data['input_cashless'].replace(',','.'))
			else:
				working_day.cashless = 0	

			working_day.save()

			current_path = request.META['HTTP_REFERER']
			return redirect(current_path)
	else:

		current_path = request.META['HTTP_REFERER']
		return redirect(current_path)	


def working_day_delete(request, day_slug):

	pass