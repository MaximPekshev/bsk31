from django.shortcuts import render, redirect

from django.contrib		 			import auth
from django.contrib.auth.models		import User
from django.contrib.auth.forms 		import AuthenticationForm
from django.contrib					import messages


def login(request):

	if request.method == 'POST':
		form 				= AuthenticationForm(request, request.POST)

		username 		= form.data.get('username')
		password 		= form.data.get('password')

		user 			= auth.authenticate(username=username, password=password)

		if user is not None:

			auth.login(request, user)

			return redirect('taxi_show_index')

		else:

			messages.info(request, 'Комбинации пароль-логин не существует! Обратитесь к администратору!')

			return redirect('taxi_show_index')
	
	return redirect('taxi_show_index')


def logout(request):

	auth.logout(request)

	return redirect('taxi_show_index')
