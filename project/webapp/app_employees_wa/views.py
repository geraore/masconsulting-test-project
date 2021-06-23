from django.shortcuts import render
from project.api.app_employees.models import Employees


# Create your views here.
def employees(request):
    employees = Employees.objects.all()
    context = {
        'employees': employees
    }
    return render(request, 'employees.html', context)