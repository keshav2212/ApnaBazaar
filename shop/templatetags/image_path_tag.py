from django import template
from shop.models import *
register = template.Library()
def impath(value):
    path = Image_Path.objects.get(product=value).path
    return path

register.filter('impath',impath)