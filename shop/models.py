from django.db import models
from django.contrib.auth.models import User
class Category(models.Model):
	name = models.CharField(max_length = 254)
	def __str__(self):
		return self.name

class product(models.Model):
	product_name=models.CharField(max_length=50)
	category=models.ForeignKey(Category, null=True, on_delete = models.CASCADE)
	subcategory=models.CharField(max_length=50,default="", blank =True)
	price=models.IntegerField(default=0)
	desc=models.CharField(max_length=100)
	pub_date=models.DateField()
	image=models.ImageField(upload_to="shop/images",default="")
	def __str__(self):
		return self.product_name

class Image_Path(models.Model):
	product = models.OneToOneField(product, on_delete= models.CASCADE)
	path = models.CharField(max_length = 254, null=True, blank=True)

class Cart(models.Model):
	product = models.ForeignKey(product, on_delete= models.CASCADE)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	quantity = models.IntegerField(default = 1)
	def __str__(self):
		return self.user.first_name +" - "+self.product.product_name

	
# Create your models here.
