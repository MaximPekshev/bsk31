# -*- coding: UTF-8 -*-
from django.urls import path
from django.contrib import admin

from django.utils.encoding import uri_to_iri
from django.utils.encoding import iri_to_uri

from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from .views import show_index
from .views import show_about_us
from .views import show_under_construct


urlpatterns = [

	path('', 					show_under_construct, name='show_under_construct'),
	path(u'главная', 			show_index, name='show_index'),
	path('about-us/', 			show_about_us, name='show_about_us'),

			]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()