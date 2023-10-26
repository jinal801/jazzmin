from django import forms
from django.contrib.auth import get_user_model

from .models import BloodDonor

User = get_user_model()


class BloodDonorForm(forms.ModelForm):
    """forms for the blood donor."""
    image = forms.ImageField(required=False)

    class Meta:
        model = BloodDonor
        fields = '__all__'


class UserForm(forms.ModelForm):
    """forms for the user."""
    date_joined = forms.CharField(required=False)

    class Meta:
        model = User
        fields = '__all__'
