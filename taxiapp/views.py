from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Driver
from .models import Working_day
from .forms import NewDriverForm
from django.contrib.auth.models import Group
from django.contrib				import messages


from django.contrib.auth.models import Group

def taxi_show_index(request):

	users_in_group = Group.objects.get(name="taxiadmin").user_set.all()

	if request.user.is_authenticated and request.user in users_in_group:

		drivers = Driver.objects.all()

		context = {

			'drivers':drivers,

		}

		return render(request, 'baseapp/base_taxi.html', context)

	else:
		
		return render(request, 'authapp/login.html')
	
def show_driver(request, slug):

	users_in_group = Group.objects.get(name="taxiadmin").user_set.all()

	if request.user.is_authenticated and request.user in users_in_group:

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
				third_name 			= dr_form.cleaned_data['third_name']
				driver_license 		= dr_form.cleaned_data['driver_license']
				car_model 			= dr_form.cleaned_data['car_model']
				car_number 			= dr_form.cleaned_data['car_number']
				rate 				= dr_form.cleaned_data['rate']

				new_driver = Driver(
					first_name=first_name, second_name=last_name, 
					third_name=third_name,
					driver_license=driver_license,
					car_number=car_number, car_model=car_model,
					rate=rate, debt=0,
					)
				new_driver.save()

				return redirect('taxi_show_index')
		else:

			return redirect('taxi_show_index')
	else:

		messages.info(request, 'У Вас не достаточно прав для доступа в данный раздел! Обратитесь к администратору!')
		return render(request, 'authapp/login.html')		