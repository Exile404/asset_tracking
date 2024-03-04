from django.urls import path
from .views import DeviceLogListCreateView, DeviceLogRetrieveUpdateDestroyView

urlpatterns = [
    path('logs/', DeviceLogListCreateView.as_view(), name='device-log-list-create'),
    path('logs/<int:pk>/', DeviceLogRetrieveUpdateDestroyView.as_view(), name='device-log-retrieve-update-destroy'),
]
