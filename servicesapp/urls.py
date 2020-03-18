from django.urls import path
from .views import show_service_objects
from .views import show_service_object

urlpatterns = [

	path('', 				show_service_objects, name='show_service_objects'),
	path('<str:slug>/', 	show_service_object, name='show_service_object'),

			]