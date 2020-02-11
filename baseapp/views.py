from django.shortcuts import render
from django.http import HttpResponse
from objectapp.models import Build_object
from objectapp.models import Picture


class Item(object):
	
	build_object 	= Build_object
	image 			= Picture


def show_index(request):

	build_objects = Build_object.objects.all().order_by('object_top')[:5]

	table = []

	for obj in build_objects:

		item = Item()
		
		item.build_object = obj
		
		images = Picture.objects.get(build_object=obj, main_image=True)
		
		item.image = images 
		 	
		table.append(item)

	template_name = 'baseapp/index.html'

	context = {

		'build_objects': table,
	}

	return render(request, template_name, context)	


def show_about_us(request):
	return render(request, 'baseapp/about_us.html')

def show_under_construct(request):
	return render(request, 'baseapp/under_construct.html')