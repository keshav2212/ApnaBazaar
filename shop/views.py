from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from math import ceil
from django.conf import settings
from django.db.models import Q
from django.contrib import messages
from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from imagekitio import ImageKit
# from django.core.cache.backends.base import DEFAULT_TIMEOUT
# from django.views.decorators.cache import cache_page
# from django.core.cache import cache

def index(request):
	filter = request.GET.get('product',None)
	context = {}
	if request.user.is_authenticated:
		cart = Cart.objects.filter(user = request.user).values('product__id')
		context['cart'] = [d['product__id'] for d in cart]
	if filter is not None:
		# if cache.get(filter):
		# 	print("Come from Cache.")
		# 	context['filter'] = cache.get('filter')
		# else:
		products=product.objects.filter(product_name__contains = filter)
		#cache.set(filter, products)
		context['filter'] = filter
	else:
		# if cache.get("all"):
		# 	print("came from cache")
		# 	products = cache.get("all")
		# else:
		products=product.objects.all()
		#cache.set("all", products)
	context['product'] = products
	context['path'] = Image_Path.objects.filter(product__in=products)
	return render(request,"shop/index.html",context)

@login_required
def addtocart(request, id):
	prod = product.objects.get(id=id)
	cart = Cart.objects.filter(Q(user = request.user) & Q(product = prod))
	if len(cart) is 0:
		instance = Cart(product = prod, user = request.user)
		instance.save()
	return redirect('/')

@login_required
def removefromcart(request, id):
	cart = Cart.objects.filter(Q(user = request.user) & Q(product__id = id))
	cart.delete()
	return redirect('/')


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

def login1(request):
	if request.method=='POST':
		lusername=request.POST['username']
		lpassword=request.POST['password']
		user=authenticate(username=lusername,password=lpassword)
		if user is not None:
			login(request,user)
			messages.success(request,"%s has been logged in Successfully"%user.username)
			return redirect('/')
		else:
			messages.error(request,'Invalid Username or Password')
			return redirect('/login')
	return render(request,'shop/login.html')



def logout1(request):
	messages.success(request,"You have been logged out Successfully")
	logout(request)
	return redirect('/')

def register(request):
	if request.method=='POST':
		username=request.POST['username']
		password=request.POST['password']
		cpassword=request.POST['password1']
		mobilenumber=request.POST['number']
		email=request.POST['email']
		if password==cpassword:
			user=User.objects.create_user(username,email,password)
			user.first_name=request.POST['firstname'] 
			user.last_name=request.POST['lastname']
			user.save()
			messages.success(request,'%s has been Registered Successfully'%user.username)
			return redirect('/login')
		else:
			messages.error(request,"Your password didn't match!")
			return redirect('/register')
	return render(request,'shop/register.html')

