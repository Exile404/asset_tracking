from django.test import TestCase
from .models import Asset

class AssetModelTest(TestCase):
    def setUp(self):
        Asset.objects.create(name='Laptop', description='Office Laptop')

    def test_asset_str_representation(self):
        laptop = Asset.objects.get(name='Laptop')
        self.assertEqual(str(laptop), 'Laptop')
