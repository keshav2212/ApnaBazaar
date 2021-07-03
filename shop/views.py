from django.shortcuts import render
from django.http import HttpResponse
from .models import product
from math import ceil
def index(request):
	filter = request.GET.get('product',None)
	context = {}
	if filter is not None:
		products=product.objects.filter(product_name__contains = filter)
		context['filter'] = filter
	else:
		products=product.objects.all()
	context['product'] = products
	return render(request,"shop/index.html",context)
def about(request):
	return render(request,"shop/about.html")
def contact(request):
	return HttpResponse("We are at contact")
def productview(request):
	return HttpResponse("We are at productview")
def checkout(request):
	return HttpResponse("We are at checkout")
def search(request):
	return HttpResponse("We are at search")
def tracker(request):
	return HttpResponse("We are at tracker")
