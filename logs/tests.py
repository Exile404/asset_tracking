from django.test import TestCase
from .models import DeviceLog
from devices.models import Device
from employees.models import Employee
from datetime import datetime

class DeviceLogModelTest(TestCase):
    def setUp(self):
        employee = Employee.objects.create(name='HRR', email='hrr@example.com', department='HR')
        device = Device.objects.create(name='Tablet', description='Company Tablet', assigned_to=employee)
        DeviceLog.objects.create(device=device, checkout_time=datetime.now(), condition_on_checkout='Good')

    def test_device_log_str_representation(self):
        log = DeviceLog.objects.first()
        expected_str_prefix = f"{log.device.name} - "
        self.assertTrue(str(log).startswith(expected_str_prefix))
