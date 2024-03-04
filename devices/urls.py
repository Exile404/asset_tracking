from django.urls import path
from .views import DeviceListCreateView, DeviceRetrieveUpdateDestroyView

urlpatterns = [
    path('devices/', DeviceListCreateView.as_view(), name='device-list-create'),
    path('devices/<int:pk>/', DeviceRetrieveUpdateDestroyView.as_view(), name='device-retrieve-update-destroy'),
]
