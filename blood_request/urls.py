from django.urls import path, include

from blood_request.views import BloodRequestView, BloodRequestListView

app_name = 'blood_request'

urlpatterns = [
    path("add_request/", BloodRequestView.as_view(), name="add_request"),
    path("list_request/", BloodRequestListView.as_view(), name="list_request")
]