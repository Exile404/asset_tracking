from django.db import models
from django.utils import timezone
from devices.models import Device

class DeviceLog(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    checkout_time = models.DateTimeField()
    return_time = models.DateTimeField(blank=True, null=True)
    condition_on_checkout = models.CharField(max_length=100)
    condition_on_return = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.device.name} - {self.checkout_time}"

    def save(self, *args, **kwargs):
        self.checkout_time = timezone.now()
        super().save(*args, **kwargs)
