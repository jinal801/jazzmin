from django.db.models.aggregates import Count
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import CreateView
from django.views.generic.list import ListView

from donor.forms import BloodDonorForm, UserForm
from donor.models import BloodGroupUser, BloodDonor


# Create your views here.
class IndexView(ListView):
    """dashboard for the donor and requester both."""
    template_name = 'index.html'
    model = BloodGroupUser
    queryset = BloodGroupUser.objects.all()
    context_object_name = 'all_group'

    def get_queryset(self):
        return BloodGroupUser.objects.annotate(total=Count('blooddonor'))


class DonorCreateView(CreateView):
    """"donor create."""
    template_name = 'become_donor.html'
    model = BloodDonor
    form_class = BloodDonorForm

    def post(self, request, *args, **kwargs):
        user_form = UserForm(self.request.POST)
        form = BloodDonorForm(self.request.POST)
        if user_form.is_valid() and form.is_valid():
            instance_user = user_form.save()
            instance_user.save()
            user_instance = instance_user
            star_form = form.save()
            star_form.donor = user_instance
            star_form.save()
        return redirect(reverse('donor:index'))