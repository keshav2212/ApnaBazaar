from .models import product, Image_Path
from django.dispatch import receiver
from django.db.models.signals import post_delete,pre_save,post_save
import os
from django.conf import settings
from imagekitio import ImageKit
from django.db import models

def post_image(image_path):
	filename = image_path.split('/')[-1]
	imagekit = ImageKit(
				private_key=settings.IMAGEKIT_PRIVATE_KEY,
				public_key=settings.IMAGEKIT_PUBLIC_KEY,
				url_endpoint=settings.IMAGEKIT_URL_ENDPOINT
	)
	upload = imagekit.upload(
	file=open(image_path, "rb"),
	file_name=filename,
	)
	try:
		image_url = upload['response']['url'] 
	except:
		image_url = "Error"
	return image_url

@receiver(post_save,sender=product)
def uploadimage(sender,instance,created,**kwargs):
    filename = instance.image.path.split('\\')[-1]
    filename = filename.split('.')[0]
    flag = 0
    if created:
        flag = 1
        url = post_image(instance.image.path)
        Image_Path(product = instance, path = url).save()
    else:
        image_path_obj = Image_Path.objects.get(product=instance)
        if filename not in image_path_obj.path:
            flag = 1
            image_path_obj.path = post_image(instance.image.path)
            image_path_obj.save()
    if flag==1:
        pathr=os.path.join('media/',str(instance.image))
        if os.path.exists(pathr) and pathr!='media/':
            os.remove(pathr)

@receiver(post_delete,sender=product)
def deletedata(sender,instance,**kwargs):
    pathr=os.path.join('media/',str(instance.image))
    if os.path.exists(pathr) and pathr!='media/':
        os.remove(pathr)