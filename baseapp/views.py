from django.shortcuts import render
from django.http import HttpResponse
from objectapp.models import Build_object
from objectapp.models import Picture

from servicesapp.models import Service_object
from certapp.models import Cert_object
from certapp.models import Picture as Cert_picture

class Item(object):
	
	build_object 	= Build_object
	image 			= Picture

class Cert_item(object):
	
	cert_object 	= Cert_object
	cert_picture 	= Cert_picture


def show_index(request):

	service_objects = Service_object.objects.all()

	build_objects = Build_object.objects.all().order_by('-object_top')[:5]

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

	template_name = 'baseapp/index.html'

	context = {

		'build_objects': table, 'service_objects': service_objects,
	}

	return render(request, template_name, context)	


def show_about_us(request):

	service_objects = Service_object.objects.all()

	context = {

		'service_objects': service_objects,
	}

	return render(request, 'baseapp/about_us.html', context)

def show_certificates(request):

	service_objects = Service_object.objects.all()

	cert_objects = Cert_object.objects.all()

	table = []

	for obj in cert_objects:

		item = Cert_item()
		
		item.cert_object = obj

		item.cert_picture = Cert_picture.objects.filter(cert_object=obj).first()	 
		 	
		table.append(item)

	context = {

		'service_objects': service_objects, 'cert_objects': table,
	}
	return render(request, 'baseapp/certificates.html', context)