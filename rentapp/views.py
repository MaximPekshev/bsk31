from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator
from .models import Rent_object
from .models import Rent_picture

from servicesapp.models import Service_object

class Item(object):
	
	rent_object 	= Rent_object
	rent_picture 	= Rent_picture

def show_rent_objects(request, category):

	service_objects = Service_object.objects.all()

	rent_object_count=20
	rent_objects = Rent_object.objects.filter(rent_category=category).order_by('object_top')
	
	table = []
	for obj in rent_objects:

		item = Item()
		
		item.rent_object = obj

		item.rent_picture = Rent_picture.objects.filter(rent_object=obj).first()
 	
		table.append(item)	

	page_number = request.GET.get('page', 1)

	paginator = Paginator(table, rent_object_count)	

	page = paginator.get_page(page_number)


	is_paginated = page.has_other_pages()

	if page.has_previous():
		prev_url = '?page={}'.format(page.previous_page_number())
	else:
		prev_url = ''	

	if page.has_next():
		next_url = '?page={}'.format(page.next_page_number())
	else:
		next_url = ''			

	template_name = 'rentapp/rent.html'
	context = {
		'page_object': page, 'prev_url': prev_url, 'next_url': next_url, 'is_paginated': is_paginated,
		'rent_category':category, 'service_objects': service_objects,
	}

	return render(request, template_name, context)

