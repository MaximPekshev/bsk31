from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Driver, Car
from .models import Working_day
from .forms import NewDriverForm
from django.contrib.auth.models import Group
from django.contrib				import messages
from .models import Cashbox
from django.db.models import Sum
from datetime import datetime
from decimal import Decimal
from workingdayapp.forms import WorkingDayForm
from django.utils import timezone
from .forms import PeriodForm, Gas_upload

from django.contrib.auth.models import Group

import django.core.exceptions

import requests
import json
import xlrd


def culc_debt(drivers):
	debt=0
	for driver in drivers:
		debt += driver.debt
	return debt


def taxi_show_index(request):

	taxiadmin = False

	users_in_group = Group.objects.get(name="taxiadmin").user_set.all()

	if request.user in users_in_group:

		taxiadmin = True

	users_in_group_collector = Group.objects.get(name="taxicollector").user_set.all()

	if request.user.is_authenticated and (request.user in users_in_group or request.user in users_in_group_collector):

		drivers_works = Driver.objects.filter(active=True).order_by('second_name')

		cars_works = []

		for dr in drivers_works:
			if dr.car in cars_works:
				pass
			else:
				if dr.car:
					cars_works.append(dr.car)

		debt_of_works = culc_debt(drivers_works)

		drivers_fired = Driver.objects.filter(active=False).order_by('second_name')

		debt_of_fired = culc_debt(drivers_fired)

		cars = Car.objects.all()

		context = {

			'drivers_works':drivers_works,
			'debt_of_works':debt_of_works,
			'drivers_fired':drivers_fired,
			'debt_of_fired':debt_of_fired,
			'cars':cars,
			'cars_works': len(cars_works),
			'taxiadmin': taxiadmin,

		}

		return render(request, 'baseapp/base_taxi.html', context)

	else:
		
		return render(request, 'authapp/login.html')
	
def show_driver(request, slug):

	users_in_group = Group.objects.get(name="taxiadmin").user_set.all()

	users_in_group_collector = Group.objects.get(name="taxicollector").user_set.all()

	if request.user.is_authenticated and (request.user in users_in_group or request.user in users_in_group_collector):

		driver = Driver.objects.get(slug = slug)

		working_days = Working_day.objects.filter(driver = driver).order_by("-date")

		if driver.car:
			cars = Car.objects.exclude(slug=driver.car.slug)
		else:
			cars = Car.objects.all()



		context = {

			'working_days': working_days, 'driver': driver, 'cars':cars,

		}

		return render(request, 'taxiapp/driver.html', context)

	else:
		messages.info(request, 'У Вас не достаточно прав для доступа в данный раздел! Обратитесь к администратору!')
		return render(request, 'authapp/login.html')

def driver_add_new(request):

	users_in_group = Group.objects.get(name="taxiadmin").user_set.all()

	if request.user.is_authenticated and request.user in users_in_group:
		
		if request.method == 'POST':

			dr_form = NewDriverForm(request.POST)

			if dr_form.is_valid():

				first_name 			= dr_form.cleaned_data['first_name']
				last_name 			= dr_form.cleaned_data['last_name']
				car_obj 			= dr_form.cleaned_data['car_obj']

				if car_obj:
					car = Car.objects.get(car_number=car_obj)
				else:
					car = None
						
				rate 				= float(dr_form.cleaned_data['rate'].replace(',','.'))

				if dr_form.cleaned_data['third_name']:
					third_name = dr_form.cleaned_data['third_name']
				else:
					third_name = ''


				if dr_form.cleaned_data['driver_license']:
					driver_license = dr_form.cleaned_data['driver_license']
				else:
					driver_license = ''

				if dr_form.cleaned_data['fuel_card']:
					fuel_card = dr_form.cleaned_data['fuel_card']
				else:
					fuel_card = ''	

				active 				= dr_form.cleaned_data['active']	

				monday 				= dr_form.cleaned_data['monday']
				tuesday 			= dr_form.cleaned_data['tuesday']
				wednesday 			= dr_form.cleaned_data['wednesday']
				thursday 			= dr_form.cleaned_data['thursday']
				friday 				= dr_form.cleaned_data['friday']
				saturday 			= dr_form.cleaned_data['saturday']
				sunday 				= dr_form.cleaned_data['sunday']

				new_driver = Driver(
					first_name=first_name, second_name=last_name, 
					third_name=third_name,
					driver_license=driver_license,
					fuel_card=fuel_card,
					rate=rate, debt=0, active=active,
					monday=monday, tuesday=tuesday, wednesday=wednesday,
					thursday=thursday, friday=friday, saturday=saturday, sunday=sunday,
					car=car,
					)
				new_driver.save()

				return redirect('taxi_show_index')
		else:

			return redirect('taxi_show_index')
	else:

		messages.info(request, 'У Вас не достаточно прав для доступа в данный раздел! Обратитесь к администратору!')
		return render(request, 'authapp/login.html')		

def driver_edit(request, slug):
			
	users_in_group = Group.objects.get(name="taxiadmin").user_set.all()

	if request.user.is_authenticated and request.user in users_in_group:
		
		if request.method == 'POST':

			dr_form = NewDriverForm(request.POST)

			if dr_form.is_valid():

				first_name 			= dr_form.cleaned_data['first_name']
				last_name 			= dr_form.cleaned_data['last_name']

				if dr_form.cleaned_data['third_name']:
					third_name 	= dr_form.cleaned_data['third_name']
				else:
					third_name 	= ''

				if dr_form.cleaned_data['driver_license']:
					driver_license 	= dr_form.cleaned_data['driver_license']
				else:
					driver_license 	= ''

				if dr_form.cleaned_data['fuel_card']:
					fuel_card = dr_form.cleaned_data['fuel_card']
				else:
					fuel_card = ''	


				car_obj 			= dr_form.cleaned_data['car_obj']

				if car_obj:
					car = Car.objects.get(car_number=car_obj)
				else:
					car = None


				rate 				= float(dr_form.cleaned_data['rate'].replace(',','.'))

				active 				= dr_form.cleaned_data['active']

				monday 				= dr_form.cleaned_data['monday']
				tuesday 			= dr_form.cleaned_data['tuesday']
				wednesday 			= dr_form.cleaned_data['wednesday']
				thursday 			= dr_form.cleaned_data['thursday']
				friday 				= dr_form.cleaned_data['friday']
				saturday 			= dr_form.cleaned_data['saturday']
				sunday 				= dr_form.cleaned_data['sunday']

				driver = Driver.objects.get(slug=slug)

				if driver.first_name != first_name:
					driver.first_name = first_name

				if driver.second_name != last_name:
					driver.second_name = last_name	

				if driver.third_name != third_name:
					driver.third_name = third_name		

				if driver.driver_license != driver_license:
					driver.driver_license = driver_license

				if driver.fuel_card != fuel_card:
					driver.fuel_card = fuel_card	

				if driver.rate != rate:
					driver.rate = rate	

				if driver.active != active:
					driver.active = active

				if driver.monday != monday:
					driver.monday = monday

				if driver.tuesday != tuesday:
					driver.tuesday = tuesday

				if driver.wednesday != wednesday:
					driver.wednesday = wednesday

				if driver.thursday != thursday:
					driver.thursday = thursday

				if driver.friday != friday:
					driver.friday = friday

				if driver.saturday != saturday:
					driver.saturday = saturday

				if driver.sunday != sunday:
					driver.sunday = sunday

				if driver.car != car:
					driver.car = car


				driver.save()

				current_path = request.META['HTTP_REFERER']
				return redirect(current_path)

		else:

			return redirect('taxi_show_index')
	else:

		messages.info(request, 'У Вас не достаточно прав для доступа в данный раздел! Обратитесь к администратору!')
		return render(request, 'authapp/login.html')			


def taxi_show_cashbox(request):

	users_in_group = Group.objects.get(name="taxiadmin").user_set.all()
	users_in_group_collector = Group.objects.get(name="taxicollector").user_set.all()

	if request.user.is_authenticated and (request.user in users_in_group or request.user in users_in_group_collector):

		cashbox = Cashbox.objects.all().order_by('-date')

		ca_cash 	 = Cashbox.objects.all().aggregate(Sum('cash'))['cash__sum']
		ca_cash_card = Cashbox.objects.all().aggregate(Sum('cash_card'))['cash_card__sum']

		context = {

			'cashbox': cashbox, 'ca_cash': ca_cash, 'ca_cash_card': ca_cash_card,

		}

		return	render(request, 'taxiapp/cashbox.html', context)

	else:

		messages.info(request, 'У Вас не достаточно прав для доступа в данный раздел! Обратитесь к администратору!')
		return render(request, 'authapp/login.html')

def taxi_incass(request):

	users_in_group = Group.objects.get(name="taxicollector").user_set.all()

	if request.user.is_authenticated and request.user in users_in_group:


		if request.method == 'POST':

			incass_form = WorkingDayForm(request.POST)

			if incass_form.is_valid():

				if incass_form.cleaned_data['input_cash']:
					cash = Decimal(incass_form.cleaned_data['input_cash'].replace(',','.'))
				else:
					cash = 0

				if incass_form.cleaned_data['input_cash_card']:
					cash_card = Decimal(incass_form.cleaned_data['input_cash_card'].replace(',','.'))
				else:
					cash_card = 0

				if cash != 0 or cash_card != 0:
			
					cashbox = Cashbox(
						date=datetime.now(),
						cash=-cash,
						cash_card=-cash_card,
						)

					cashbox.save()

					current_path = request.META['HTTP_REFERER']
					return redirect(current_path)

				else:		
					current_path = request.META['HTTP_REFERER']
					return redirect(current_path)

			else:		
				current_path = request.META['HTTP_REFERER']
				return redirect(current_path)		

		else:		
			current_path = request.META['HTTP_REFERER']
			return redirect(current_path)			

	else:

		messages.info(request, 'У Вас не достаточно прав для доступа в данный раздел! Обратитесь к администратору!')
		return render(request, 'authapp/login.html')


def taxi_show_history(request):
	
	users_in_group = Group.objects.get(name="taxiadmin").user_set.all()
	users_in_group_collector = Group.objects.get(name="taxicollector").user_set.all()

	if request.user.is_authenticated and (request.user in users_in_group or request.user in users_in_group_collector):

		if request.method == 'POST':

			period_form = PeriodForm(request.POST)

			if period_form.is_valid():

				trip_start 		= period_form.cleaned_data['trip_start'] + ' 00:00:01'
				trip_end 		= period_form.cleaned_data['trip_end'] + ' 23:59:59'

				date_lte 	= datetime.strptime(trip_start, '%Y-%m-%d %H:%M:%S')
				date_now	= datetime.strptime(trip_end, '%Y-%m-%d %H:%M:%S')

			else:

				messages.info(request, 'Не выбран период отчета!!')
				current_path = request.META['HTTP_REFERER']
				return redirect(current_path)	

		else:

			date_now    =   timezone.now()

			if date_now.day > 7:

				date_lte 	= 	date_now.replace(day = int(date_now.day - 7))

			else:	

				date_lte 	= 	date_now.replace(day = int(date_now.day + 30 - 7))

				if date_now.month > 1:

					date_lte 	= 	date_lte.replace(month = int(date_lte.month - 1))

				else:

					date_lte 	= 	date_lte.replace(month = int(date_lte.month + 12 - 1))
					date_lte 	= 	date_lte.replace(year = int(date_lte.year - 1))
					

		d_history = []

		driver_history = Driver.history.filter(history_date__lte=date_now, history_date__gte=date_lte)

		for dh in driver_history:

			try:

				dr_prev = dh.get_previous_by_history_date(id=dh.id)

				driver 			= False
				if (dh.first_name != dr_prev.first_name):

					driver 		= True

				if (dh.second_name != dr_prev.second_name):

					driver 		= True

				if (dh.third_name != dr_prev.third_name):

					driver 		= True	

				driver_license 	= False if (dh.driver_license == dr_prev.driver_license) else True
				rate 			= False if (dh.rate == dr_prev.rate) else True
				fuel_card 		= False if (dh.fuel_card == dr_prev.fuel_card) else True
				car 			= False if (dh.car == dr_prev.car) else True

			except dh.DoesNotExist:


				driver 			= False
				driver_license 	= False
				rate			= False
				fuel_card		= False
				car 			= False

			d_history.append([dh, driver, driver_license, rate, fuel_card, car])

		work_day_hist  = []

		wd_history     = Working_day.history.filter(history_date__lte=date_now, history_date__gte=date_lte)

		for wd in wd_history:

			try:

				wd_prev 		= wd.get_previous_by_history_date(id=wd.id)

				rate 			= False if (wd.rate == wd_prev.rate) else True
				fuel 			= False if (wd.fuel == wd_prev.fuel) else True
				penalties 		= False if (wd.penalties == wd_prev.penalties) else True
				cash 			= False if (wd.cash == wd_prev.cash) else True
				cash_card 		= False if (wd.cash_card == wd_prev.cash_card) else True
				cashless 		= False if (wd.cashless == wd_prev.cashless) else True
				debt_of_day 	= False if (wd.debt_of_day == wd_prev.debt_of_day) else True


			except wd.DoesNotExist:

				rate 			= False
				fuel 			= False
				penalties 		= False
				cash 			= False
				cash_card 		= False
				cashless		= False
				debt_of_day 	= False

			work_day_hist.append([wd, rate, fuel, penalties, cash, cash_card, cashless, debt_of_day])	


		context = {

			'd_history': d_history,
			'work_day_hist': work_day_hist,
			'date_now': date_now.strftime("%Y-%m-%d"),
			'date_lte': date_lte.strftime("%Y-%m-%d"),
		}

		return	render(request, 'taxiapp/history.html', context)

	else:

		messages.info(request, 'У Вас не достаточно прав для доступа в данный раздел! Обратитесь к администратору!')
		return render(request, 'authapp/login.html')


def gas_upload(request):

	users_in_group = Group.objects.get(name="taxiadmin").user_set.all()

	if request.user.is_authenticated and request.user in users_in_group:
		
		if request.method == 'POST':

			gas_form = Gas_upload(request.POST,request.FILES)

			if gas_form.is_valid():

				gas_file = 	request.FILES['gas_file']
				option_gas = request.POST['optiongas']

				missing_drivers = []
				upload_transactions = []

				wb = xlrd.open_workbook(file_contents=gas_file.read())

				sheet = wb.sheet_by_index(0)

				if option_gas == 'option1':

					for n in range(sheet.nrows):

						if sheet.cell(n,4).value == 'Дебет':

							date_of_transaction = datetime.date(xlrd.xldate.xldate_as_datetime(sheet.cell(n,0).value, wb.datemode))

							fuel_card = str(int(sheet.cell(n,2).value))

							summ_of_transaction = Decimal(abs(sheet.cell(n,9).value)).quantize(Decimal("1.00"))

							taxidriver = Driver.objects.filter(fuel_card=fuel_card).first()

							if taxidriver:

								working_day = Working_day.objects.filter(driver=taxidriver, date=date_of_transaction).first()

								if working_day:
									working_day.fuel = working_day.fuel + summ_of_transaction
									working_day.save()
								else:	
									working_day = Working_day.objects.filter(driver=taxidriver).last()
									working_day.fuel = working_day.fuel + summ_of_transaction
									working_day.save()

								upload_transactions.append([date_of_transaction, taxidriver.second_name, taxidriver.first_name, fuel_card, summ_of_transaction])

							else:

								missing_drivers.append([date_of_transaction, fuel_card, summ_of_transaction])

				elif option_gas == 'option2':

					def_fuel_card = ''

					for n in range(sheet.nrows):

						if sheet.cell(n,5).value == 'Обслуживание':

							date_of_transaction = datetime.strptime(sheet.cell(n,4).value, '%d.%m.%Y %H:%M:%S').date()

							if sheet.cell(n,0).value:

								fuel_card = str(int(sheet.cell(n,0).value))

								def_fuel_card = fuel_card

							else:
								
								fuel_card = def_fuel_card

							summ_of_transaction = Decimal(abs(sheet.cell(n,11).value)).quantize(Decimal("1.00"))

							taxidriver = Driver.objects.filter(fuel_card=fuel_card).first()

							if taxidriver:

								working_day = Working_day.objects.filter(driver=taxidriver, date=date_of_transaction).first()

								if working_day:
									working_day.fuel = working_day.fuel + summ_of_transaction
									working_day.save()
								else:	
									working_day = Working_day.objects.filter(driver=taxidriver).last()
									working_day.fuel = working_day.fuel + summ_of_transaction
									working_day.save()

								upload_transactions.append([date_of_transaction, taxidriver.second_name, taxidriver.first_name, fuel_card, summ_of_transaction])

							else:

								missing_drivers.append([date_of_transaction, fuel_card, summ_of_transaction])

				context = {
							'upload_transactions': upload_transactions,
							'missing_drivers': missing_drivers,
				}

				return	render(request, 'taxiapp/upload_succes.html', context)

			else:
				current_path = request.META['HTTP_REFERER']
				return redirect(current_path)

		else:
			current_path = request.META['HTTP_REFERER']
			return redirect(current_path)
	else:

		messages.info(request, 'У Вас не достаточно прав для доступа в данный раздел! Обратитесь к администратору!')
		return render(request, 'authapp/login.html')			