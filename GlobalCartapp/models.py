from django.db import models
from django.contrib.auth.models import User
from GlobalCartapp.choices import *
import datetime


# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(blank=True, null=True, upload_to="covers/")
    price = models.IntegerField()
    availability = models.IntegerField()
    rating = models.IntegerField()
    description = models.TextField()
    ordercount = models.IntegerField()
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class userinfo(models.Model):
    user = models.ForeignKey(User, models.CASCADE)
    address = models.TextField()
    wallet = models.CharField(max_length=20)
    phonenumber = models.CharField(max_length=20)

    def __str__(self):
        return self.user.username


class addtocart(models.Model):
    item = models.ForeignKey(Item, models.CASCADE)
    user = models.ForeignKey(User, models.CASCADE)
    price = models.IntegerField()
    image = models.ImageField(blank=True, null=True, upload_to="covers/")
    quantity = models.IntegerField()


class Itemreviews(models.Model):
    item = models.ForeignKey(Item, models.CASCADE)
    user = models.ForeignKey(User, models.CASCADE)
    reviews = models.TextField()
    rating = models.IntegerField(choices=RATING_CHOICES, default=1)


class Bookedinfo(models.Model):
    item = models.ForeignKey(Item, models.CASCADE)
    user = models.ForeignKey(User, models.CASCADE)
    price = models.IntegerField()
    image = models.ImageField(blank=True, null=True, upload_to="covers/")
    quantity = models.IntegerField()
    time = models.DateTimeField(default=datetime.datetime.today(), blank=True)


class wishlist(models.Model):
    item = models.ForeignKey(Item, models.CASCADE)
    user = models.ForeignKey(User, models.CASCADE)
    image = models.ImageField(blank=True, null=True, upload_to="covers/")
    price = models.IntegerField()


class preorder(models.Model):
    item = models.ForeignKey(Item, models.CASCADE)
    user = models.ForeignKey(User, models.CASCADE)
    image = models.ImageField(blank=True, null=True, upload_to="covers/")
    price = models.IntegerField()


class Payment(models.Model):
    user = models.ForeignKey(User, models.CASCADE)
    item = models.ForeignKey(Item, models.CASCADE)
    Name_on_card = models.CharField(max_length=50)
    cardno = models.CharField(max_length=30)
    cvv = models.CharField(max_length=3)
    # expiry_date = models.DateField(blank=True)
