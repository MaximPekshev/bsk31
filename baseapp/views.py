from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def show_index(request):
	return render(request, 'baseapp/index.html')

def show_about_us(request):
	return render(request, 'baseapp/about_us.html')
