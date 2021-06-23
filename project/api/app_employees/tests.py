from django.test import TestCase
from project.api.app_employees.models import Employees
from project.utils.employee_utils import completeEmployeeInfo


# Create your tests here.
class AnnualSalaryTestCase(TestCase):

    def setUp(self):
        Employees.objects.create(id=98, name='testcase', contract_type_name='HourlySalaryEmployee', hourly_salary=100,
                                 monthly_salary=50000)
        Employees.objects.create(id=99, name='testcase', contract_type_name='MonthlySalaryEmployee', hourly_salary=45,
                                 monthly_salary=2500)

    def test_annual_salary(self):
        hourly_employee = completeEmployeeInfo(Employees.objects.get(id=98))
        monthly_employee = completeEmployeeInfo(Employees.objects.get(id=99))
        self.assertEqual(hourly_employee.annual_salary, 144000)
        self.assertEqual(monthly_employee.annual_salary, 30000)

