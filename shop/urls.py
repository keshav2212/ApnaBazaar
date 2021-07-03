from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
path("",views.index,name="ShopHome"),
path("about/",views.about,name="AboutUs"),
path("contact/",views.contact,name="ContactUs"),
path("tracker/",views.tracker,name="Tracker"),
path("productview/",views.productview,name="ProductView"),
path("checkout/",views.checkout,name="Checkout"),
]
