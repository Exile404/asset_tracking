from django.test import TestCase
from .models import Employee

class EmployeeModelTest(TestCase):
    def setUp(self):
        Employee.objects.create(name='Test1', email='test1@example.com', department='IT')

    def test_employee_str_representation(self):
        john = Employee.objects.get(name='Test1')
        self.assertEqual(str(john), 'Test1')
