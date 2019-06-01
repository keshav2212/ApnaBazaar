from django.db import models
class product(models.Model):
	product_id=models.AutoField
	product_name=models.CharField(max_length=50)
	desc=models.CharField(max_length=100)
	pub_date=models.DateField()

# Create your models here.
