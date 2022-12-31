from django.db import models

class user_data(models.Model):
    name=models.CharField(max_length=20)
    age=models.IntegerField(max_length=20)
    image=models.ImageField(upload_to="image",default=None)
    image1=models.ImageField(upload_to="image",default=None)
    image2=models.ImageField(upload_to="image",default=None)
    image3=models.ImageField(upload_to="image",default=None)
