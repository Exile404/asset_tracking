from rest_framework import serializers
from .models import DeviceLog

class DeviceLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceLog
        fields = ['id', 'device', 'checkout_time', 'return_time', 'condition_on_checkout', 'condition_on_return', 'created_at']
