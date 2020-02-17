from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Category(models.Model):
    name = models.CharField(max_length=128)


class Institution(models.Model):
    FOUNDATION = 1
    ORGANISATION = 2
    LOCAL = 3
    TYPE_CHOICES = (
        (FOUNDATION, 'Fundacja'),
        (ORGANISATION, 'Organizacja pozarządowa'),
        (LOCAL, 'Zbiórka lokalna'),
    )
    name = models.CharField(max_length=128)
    description = models.TextField()
    type = models.IntegerField(choices=TYPE_CHOICES, default=FOUNDATION)
    categories = models.ManyToManyField('Category')


class Donation(models.Model):
    quantity = models.IntegerField()
    categories = models.ManyToManyField('Category')
    institution = models.ForeignKey('Institution', on_delete=models.CASCADE)
    address = models.CharField(max_length=128)
    phone_number = models.IntegerField()
    city = models.CharField(max_length=128)
    zip_code = models.CharField(max_length=6)
    pick_up_date = models.DateField()
    pick_up_time = models.TimeField()
    pick_up_comment = models.TextField()
    user = models.ForeignKey(User, null=True, default=None, on_delete=models.CASCADE)
