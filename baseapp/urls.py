# -*- coding: UTF-8 -*-
from django.urls import path
from django.contrib import admin

from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from .views import show_index
from .views import show_about_us
from .views import show_under_construct
from .views import show_certificates


urlpatterns = [

	path('', 					show_under_construct, name='show_under_construct'),
	path('home/', 				show_index, name='show_index'),
	path('about-us/', 			show_about_us, name='show_about_us'),
	path('certificates/', 		show_certificates, name='show_certificates'),

			]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()