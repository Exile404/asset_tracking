from rest_framework import generics
from .models import DeviceLog
from .serializers import DeviceLogSerializer

class DeviceLogListCreateView(generics.ListCreateAPIView):
    queryset = DeviceLog.objects.all()
    serializer_class = DeviceLogSerializer

class DeviceLogRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = DeviceLog.objects.all()
    serializer_class = DeviceLogSerializer
