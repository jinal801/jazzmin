from django.contrib.auth.models import User
from django.db import models


class BloodGroupUser(models.Model):
    name = models.CharField(max_length=5)

    def __str__(self):
        return self.name


# Create your models here.
class BloodDonor(models.Model):
    donor = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    date_of_birth = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    address = models.TextField(max_length=500, default="")
    blood_group = models.ForeignKey(BloodGroupUser, on_delete=models.CASCADE)
    gender = models.CharField(max_length=10)
    image = models.ImageField(upload_to="")
    ready_to_donate = models.BooleanField(default=True)

    def __str__(self):
        return str(self.blood_group)