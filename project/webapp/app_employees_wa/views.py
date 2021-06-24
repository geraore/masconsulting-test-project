from django.shortcuts import render
from project.api.app_employees.models import Employees
from project.webapp.app_employees_wa.forms import SearchEmployeeForm


# Create your views here.
def get_employees(request):
    context = None
    if request.method == 'POST':
        form = SearchEmployeeForm(request.POST)
        if form.is_valid():
            search_value = form['search_field'].value()
            if search_value == '':
                employees = Employees.objects.all()
            else:
                employees = Employees.objects.filter(id=search_value)

            context = {
                'employees': employees,
                'form': form,
                'has_value': 1
            }
    if not context:
        form = SearchEmployeeForm
        context = {
            'employees': [],
            'form': form,
            'has_value': 0
        }

    return render(request, 'employees.html', context)