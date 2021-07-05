from django.shortcuts import render
from django.http import HttpResponse
from .models import product
from math import ceil
# from django.core.cache.backends.base import DEFAULT_TIMEOUT
# from django.views.decorators.cache import cache_page
# from django.core.cache import cache
def index(request):
	filter = request.GET.get('product',None)
	context = {}
	if filter is not None:
		# if cache.get(filter):
		# 	print("Come from Cache.")
		# 	context['filter'] = cache.get('filter')
		# else:
		products=product.objects.filter(product_name__contains = filter)
		cache.set(filter, products)
		context['filter'] = filter
	else:
		# if cache.get("all"):
		# 	print("came from cache")
		# 	products = cache.get("all")
		# else:
		products=product.objects.all()
		cache.set("all", products)
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
