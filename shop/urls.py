from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
path("",views.index,name="home"),
path("aboutus/",views.about,name="AboutUs"),
path("contact/",views.contact,name="ContactUs"),
path("tracker/",views.tracker,name="Tracker"),
path("productview/",views.productview,name="ProductView"),
path("checkout/",views.checkout,name="Checkout"),
path('login',views.login1,name='login'),
path('logout',views.logout1,name='logout'),
path('register',views.register,name='register'),    
]
