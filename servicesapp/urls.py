from django.urls import path

from .views import show_services
from .views import show_service_object

urlpatterns = [

	# path('', 				show_services, name='show_services'),
	path('<str:slug>/', 	show_service_object, name='show_service_object'),
	
			]