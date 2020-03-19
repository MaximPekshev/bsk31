from django import forms
 
class NewDriverForm(forms.Form):

	first_name  	= forms.CharField(max_length = 30)
	last_name  		= forms.CharField(max_length = 30)
	third_name  	= forms.CharField(max_length = 30, required=False)
	driver_license 	= forms.CharField(max_length = 15, required=False)
	fuel_card 		= forms.CharField(max_length = 30, required=False)
	car_model		= forms.CharField(max_length = 30)
	car_number		= forms.CharField(max_length = 15)
	rate			= forms.CharField(max_length = 15)

	active 			= forms.BooleanField(required=False)

	monday 			= forms.BooleanField(required=False)
	tuesday 		= forms.BooleanField(required=False)
	wednesday 		= forms.BooleanField(required=False)
	thursday 		= forms.BooleanField(required=False)
	friday 			= forms.BooleanField(required=False)
	saturday 		= forms.BooleanField(required=False)
	sunday 			= forms.BooleanField(required=False)