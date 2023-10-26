from django.urls import path, include

from donor.views import IndexView, DonorCreateView

app_name = 'donor'

urlpatterns = [
    path("index/", IndexView.as_view(), name="index"),
    path("add_donor/", DonorCreateView.as_view(), name="add_donor"),

]