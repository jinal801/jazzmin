from django.db import models

from donor.models import BloodGroupUser


# Create your models here.
class RequestBlood(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    state = models.CharField(max_length=200, blank=True)
    city = models.CharField(max_length=300, blank=True)
    address = models.CharField(max_length=500, blank=True)
    blood_group = models.ForeignKey(BloodGroupUser, on_delete=models.CASCADE)
    date = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name