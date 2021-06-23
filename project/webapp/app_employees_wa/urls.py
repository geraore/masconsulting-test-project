from django.urls import path
from project.webapp.app_employees_wa import views

urlpatterns = [
    path('employee/', views.employees, name='employeesQuery'),
]