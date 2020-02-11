
from django.urls import path
from django.contrib import admin

from django.conf import settings
from .views import show_objects
from .views import show_build_object



urlpatterns = [

	path('', 					show_objects, name='show_objects'),
	path('<str:slug>/', 		show_build_object, name='show_build_object'),

			]
