from django.shortcuts import render
from django.http import HttpResponse
from .models import product
from math import ceil
def index(request):
	products=product.objects.all()
	n=len(products)
	nslides=(n//4)+(ceil(n/4)-n//4)
	param={'no_of_slides':nslides,'range':range(1,nslides),'product':products}
	return render(request,"shop/index.html",param)
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

# Create your views here.
