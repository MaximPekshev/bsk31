from django.urls import path
from django.urls import include
from .views import taxi_show_index
from .views import show_driver, driver_add_new


urlpatterns = [

	path('', 						taxi_show_index, name='taxi_show_index'),
	path('driver/<str:slug>/', 		show_driver, name='show_driver'),
	path('new-driver/', 			driver_add_new, name='driver_add_new'),
	path('profile/', 				include('authapp.urls')),

			]
