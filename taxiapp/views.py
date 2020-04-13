from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Driver
from .models import Working_day
from .forms import NewDriverForm
from django.contrib.auth.models import Group
from django.contrib				import messages
from .models import Cashbox
from django.db.models import Sum
from datetime import datetime
from decimal import Decimal
from workingdayapp.forms import WorkingDayForm


from django.contrib.auth.models import Group

def taxi_show_index(request):

	users_in_group = Group.objects.get(name="taxiadmin").user_set.all()

	users_in_group_collector = Group.objects.get(name="taxicollector").user_set.all()

	if request.user.is_authenticated and (request.user in users_in_group or request.user in users_in_group_collector):

		drivers = Driver.objects.all()

		context = {

			'drivers':drivers,

		}

		return render(request, 'baseapp/base_taxi.html', context)

	else:
		
		return render(request, 'authapp/login.html')
	
def show_driver(request, slug):

	users_in_group = Group.objects.get(name="taxiadmin").user_set.all()

	users_in_group_collector = Group.objects.get(name="taxicollector").user_set.all()

	if request.user.is_authenticated and (request.user in users_in_group or request.user in users_in_group_collector):

		driver = Driver.objects.get(slug = slug)

		working_days = Working_day.objects.filter(driver = driver).order_by("date")


		context = {

			'working_days': working_days, 'driver': driver,

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
				car_model 			= dr_form.cleaned_data['car_model']
				car_number 			= dr_form.cleaned_data['car_number']
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
					car_number=car_number, car_model=car_model,
					fuel_card=fuel_card,
					rate=rate, debt=0, active=active,
					monday=monday, tuesday=tuesday, wednesday=wednesday,
					thursday=thursday, friday=friday, saturday=saturday, sunday=sunday,
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

				car_model 			= dr_form.cleaned_data['car_model']
				car_number 			= dr_form.cleaned_data['car_number']
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

				if driver.car_model != car_model:
					driver.car_model = car_model

				if driver.fuel_card != fuel_card:
					driver.fuel_card = fuel_card	
						
				if driver.car_number != car_number:
					driver.car_number = car_number

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

		cashbox = Cashbox.objects.all().order_by('date')

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
						date=datetime.today(),
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

		driver_history = Driver.history.all()
		wd_history     = Working_day.history.all()

		context = {

			'driver_history': driver_history,
			'wd_history': wd_history,
		}

		return	render(request, 'taxiapp/history.html', context)

	else:

		messages.info(request, 'У Вас не достаточно прав для доступа в данный раздел! Обратитесь к администратору!')
		return render(request, 'authapp/login.html')