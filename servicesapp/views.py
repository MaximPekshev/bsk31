from django.shortcuts import render

from .models import Service_object
from .models import Service_picture


def show_service_objects(request):

	service_objects = Service_object.objects.all()
	s_objects 		= Service_object.objects.all().order_by('-object_top')
		
	template_name = 'servicesapp/services.html'

	context = {
		'service_objects': service_objects, 's_objects': s_objects,
	}

	return render(request, template_name, context)

def show_service_object(request, slug):

	service_objects = Service_object.objects.all()
	
	s_object = Service_object.objects.get(object_slug=slug)

	s_picture  = Service_picture.objects.filter(service_object=s_object).first()

	template_name = 'servicesapp/service_object.html'

	context = {
		'service_objects': service_objects, 's_object':s_object, 's_picture': s_picture,
	}

	return render(request, template_name, context)	