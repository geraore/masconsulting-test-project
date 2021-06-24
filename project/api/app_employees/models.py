from django.db import models


# Create your models here.
class MyApis(models.Model):
    class Meta():
        db_table = 'my_apis'

    id = models.AutoField(primary_key=True)
    dns_name = models.TextField(db_column='dns_name')
    description = models.TextField(db_column='description')


class MyEndpoints(models.Model):
    class Meta():
        db_table = 'my_endpoints'

    id = models.AutoField(primary_key=True)
    api_id = models.ForeignKey(MyApis, on_delete=models.SET_NULL, null=True, db_column='api_id')
    path = models.TextField(db_column='path')
    description = models.TextField(db_column='description')
    descriptor = models.TextField(db_column='descriptor')


class Employees(models.Model):
    class Meta():
        db_table = 'employees'

    id = models.IntegerField(primary_key=True)
    name = models.TextField(db_column='name')
    contract_type_name = models.TextField(db_column='contractTypeName')
    role_id = models.IntegerField(db_column='roleId')
    role_name = models.TextField(db_column='roleName')
    role_description = models.TextField(db_column='roleDescription')
    hourly_salary = models.FloatField(db_column='hourlySalary')
    monthly_salary = models.FloatField(db_column='monthlySalary')
    annual_salary = 0

    def map(self, json_element):
        self.name = json_element['name']
        self.contract_type_name = json_element['contractTypeName']
        self.role_id = json_element['roleId']
        self.role_name = json_element['roleName']
        self.role_description = json_element['roleDescription']
        self.hourly_salary = json_element['hourlySalary']
        self.monthly_salary = json_element['monthlySalary']

    def serialize(self):
        return {'id': self.id,
                'name': self.name,
                'contractTypeName': self.contract_type_name,
                'roleId': self.role_id,
                'roleName': self.role_name,
                'roleDescription': self.role_description,
                'hourlySalary': self.hourly_salary,
                'monthlySalary': self.monthly_salary,
                'annualSalary': self.annual_salary}

