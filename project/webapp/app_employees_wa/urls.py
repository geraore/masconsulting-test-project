from django.urls import path
from project.webapp.app_employees_wa import views

urlpatterns = [
    path('search_employee/', views.get_employees, name='searchEmployee'),
]