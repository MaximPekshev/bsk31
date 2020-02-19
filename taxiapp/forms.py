from django import forms
 
class NewDriverForm(forms.Form):

	first_name  	= forms.CharField(max_length = 50)
	last_name  		= forms.CharField(max_length = 50)
	third_name  	= forms.CharField(max_length = 50)
	driver_license 	= forms.CharField(max_length = 50)
	car_model		= forms.CharField(max_length = 50)
	car_number		= forms.CharField(max_length = 50)
	rate			= forms.CharField(max_length = 50)
