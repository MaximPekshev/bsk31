from django import forms
 
class NewDriverForm(forms.Form):

	first_name  	= forms.CharField(max_length = 30)
	last_name  		= forms.CharField(max_length = 30)
	third_name  	= forms.CharField(max_length = 30, required=False)
	driver_license 	= forms.CharField(max_length = 15, required=False)
	fuel_card 		= forms.CharField(max_length = 30, required=False)
	rate			= forms.CharField(max_length = 15)

	active 			= forms.BooleanField(required=False)

	monday 			= forms.BooleanField(required=False)
	tuesday 		= forms.BooleanField(required=False)
	wednesday 		= forms.BooleanField(required=False)
	thursday 		= forms.BooleanField(required=False)
	friday 			= forms.BooleanField(required=False)
	saturday 		= forms.BooleanField(required=False)
	sunday 			= forms.BooleanField(required=False)
	car_obj			= forms.CharField(max_length = 10, required=False)
	
class PeriodForm(forms.Form):

	trip_start  	= forms.CharField(max_length = 12)
	trip_end  		= forms.CharField(max_length = 12)


class Gas_upload(forms.Form):

	gas_file 		= forms.FileField()
	optiongas		= forms.CharField(max_length = 30)

	