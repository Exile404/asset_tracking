from rest_framework import serializers
from .models import Device

class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = ['id', 'name', 'description', 'assigned_to', 'condition', 'checkout_time', 'return_time', 'created_at', 'updated_at']
