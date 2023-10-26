from django import forms
from .models import RequestBlood


class BloodRequestForm(forms.ModelForm):
    """forms for the blood request."""

    class Meta:
        model = RequestBlood
        fields = '__all__'