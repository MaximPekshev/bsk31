from django.urls import path
from django.urls import include
from .views import taxi_show_index
from .views import show_driver, driver_add_new, driver_edit
from .views import taxi_show_cashbox, taxi_incass
from .views import taxi_show_history
from .views import gas_upload, send_debts

urlpatterns = [

	path('', 						taxi_show_index, name='taxi_show_index'),
	path('cashbox/', 				taxi_show_cashbox, name='taxi_show_cashbox'),
	path('history/', 				taxi_show_history, name='taxi_show_history'),
	path('incass/', 				taxi_incass, name='taxi_incass'),
	path('driver/<str:slug>/', 		show_driver, name='show_driver'),
	path('new-driver/', 			driver_add_new, name='driver_add_new'),
	path('edit-driver/<str:slug>/', driver_edit, name='driver_edit'),
	path('gas-upload/', 			gas_upload, name='gas_upload'),
	path('profile/', 				include('authapp.urls')),
	path('working-days/', 			include('workingdayapp.urls')),
	path('cars/', 					include('carsapp.urls')),
	path('send-debts/', 			send_debts, name='send_debts'),

			]
