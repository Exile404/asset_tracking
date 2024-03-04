from django.test import TestCase
from .models import Employee

class EmployeeModelTest(TestCase):
    def setUp(self):
        Employee.objects.create(name='John Doe', email='john@example.com', department='IT')

    def test_employee_str_representation(self):
        john = Employee.objects.get(name='John Doe')
        self.assertEqual(str(john), 'John Doe')
