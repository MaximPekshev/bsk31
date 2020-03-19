from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator
from .models import Build_object
from .models import Picture

from servicesapp.models import Service_object

class Item(object):
	
	build_object 	= Build_object
	image 			= Picture

def show_objects(request):

	service_objects = Service_object.objects.all()

	build_object_count=10
	build_objects = Build_object.objects.all().order_by('-object_top')
	
	table = []
	for obj in build_objects:

		item = Item()
		
		item.build_object = obj

		try:
			images = Picture.objects.get(build_object=obj, main_image=True)
			item.image = images 
		except Picture.DoesNotExist:
			item.image = None
		 	
		table.append(item)	

	page_number = request.GET.get('page', 1)

	paginator = Paginator(table, build_object_count)	

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

	template_name = 'objectapp/objects.html'
	context = {
		'page_object': page, 'prev_url': prev_url, 'next_url': next_url, 'is_paginated': is_paginated,
		'service_objects': service_objects,
	}

	return render(request, template_name, context)


def show_build_object(request, slug):

	service_objects = Service_object.objects.all()

	build_object = Build_object.objects.get(object_slug=slug)

	try:
		main_picture = Picture.objects.filter(build_object=build_object).order_by('-main_image')[0]
	except IndexError:
		main_picture = None

	pictures = Picture.objects.filter(build_object=build_object, main_image=False)


	template_name = 'objectapp/build_object.html'
	context = {
		'build_object': build_object, 'pictures': pictures, 'main_picture': main_picture, 
		'service_objects': service_objects,
			}
	return render(request, template_name, context)