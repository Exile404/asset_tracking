from django.test import TestCase
from .models import Device

class DeviceModelTest(TestCase):
    def setUp(self):
        Device.objects.create(name='Phone', description='Company Phone')

    def test_device_str_representation(self):
        phone = Device.objects.get(name='Phone')
        self.assertEqual(str(phone), 'Phone')
