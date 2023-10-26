from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView

from blood_request.forms import BloodRequestForm
from blood_request.models import RequestBlood


# Create your views here.
class BloodRequestView(CreateView):
    """Create view for the blood request."""
    model = RequestBlood
    form_class = BloodRequestForm
    template_name = 'request_blood.html'

    def get_context_data(self, **kwargs):
        data = super(BloodRequestView, self).get_context_data()
        if self.request.POST:
            data['form'] = self.form_class(self.request.POST)
        else:
            data['form'] = self.form_class()
        return data

    def form_valid(self, form):
        """
        This method will be used for validating forms.
        """
        context = self.get_context_data()
        form = context['form']
        # resource data validation as form at time of creating user object
        form.save()
        return redirect('donor:index')


class BloodRequestListView(ListView):
    """blood request listing."""
    template_name = 'see_all_request.html'
    model = RequestBlood
    queryset = RequestBlood.objects.all()
    context_object_name = 'requests'

