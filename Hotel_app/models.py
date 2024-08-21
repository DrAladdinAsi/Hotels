from django.db import models

# Create your models here.

class HotelImages(models.Model):
    h_name=models.CharField(max_length=50,null=True,blank=True)
    images=models.ImageField(upload_to="hotels_ph",null=True,blank=True)
    def __str__(self):
        return self.h_name
    
class Hotel(models.Model):
    name=models.CharField(max_length=50,null=True,blank=True)
    city=models.CharField(max_length=50,null=True,blank=True)
    h_type=models.CharField(max_length=50,null=True,blank=True)
    address=models.CharField(max_length=500,null=True,blank=True)
    H_photo=models.ImageField(upload_to="hotels_ph",null=True,blank=True)
    price=models.IntegerField(null=True,blank=True)
    description=models.TextField(null=True,blank=True)
    size=models.IntegerField(null=True,blank=True)
    bed_num=models.IntegerField(null=True,blank=True)
    bathroom=models.IntegerField(null=True,blank=True)
    musuem_dest=models.IntegerField(null=True,blank=True)
    stations_dest=models.IntegerField(null=True,blank=True)
    resturant_dest=models.IntegerField(null=True,blank=True)
    rate=models.IntegerField(null=True,blank=True)
    latitude=models.DecimalField(max_digits=10,decimal_places=7,null=True,blank=True)
    longitude=models.DecimalField(max_digits=10,decimal_places=7,null=True,blank=True)
    H_photos=models.ManyToManyField(HotelImages)

    def __str__(self):
        return self.name