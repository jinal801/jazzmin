from django.contrib import admin

from donor.models import BloodDonor, BloodGroupUser


# Register your models here.
admin.site.register(BloodDonor)
admin.site.register(BloodGroupUser)