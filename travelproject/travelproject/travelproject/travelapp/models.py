from django.db import models

# Create your models here.
class Place(models.Model):
    name=models.CharField(max_length=250)
    img=models.ImageField(upload_to='pics')
    desc=models.TextField()
    def __str__(self):
        return self.name
class Profile(models.Model):
    names= models.CharField(max_length=250)
    imgs=models.ImageField(upload_to='port')
    descr=models.TextField()
    def __str__(self):
        return self.names