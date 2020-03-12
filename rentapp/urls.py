from django.urls import path
from .views import show_rent_objects


urlpatterns = [

	path('<str:category>/', 					show_rent_objects, name='show_rent_objects'),

			]