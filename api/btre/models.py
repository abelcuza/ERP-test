from django.db import models
from datetime import datetime, date



class Realtor(models.Model):
    name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to=f'images/realtors/')
    description = models.TextField(blank=True)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=20)
    hire_date = models.DateField(default=date.today(), blank=True)
    is_mvp = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Listing(models.Model):
    realtor = models.ForeignKey(Realtor, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200)
    adress = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=20)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    garage = models.IntegerField(default=0)
    sqft = models.IntegerField()
    lot_size = models.DecimalField(max_digits=5, decimal_places=1)
    photo_main = models.ImageField(upload_to=f'images/houses/')
    photo_1 = models.ImageField(upload_to=f'images/houses/', blank=True)
    photo_2 = models.ImageField(upload_to=f'images/houses/', blank=True)
    photo_3 = models.ImageField(upload_to=f'images/houses/', blank=True)
    photo_4 = models.ImageField(upload_to=f'images/houses/', blank=True)
    photo_5 = models.ImageField(upload_to=f'images/houses/', blank=True)
    photo_6 = models.ImageField(upload_to=f'images/houses/', blank=True)
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title


class Contact(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=20)
    message = models.TextField(blank=True)
    contact_date = models.DateField(default=date.today(), blank=True)

    def __str__(self):
        return self.name
