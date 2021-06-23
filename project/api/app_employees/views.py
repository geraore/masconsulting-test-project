from rest_framework_api_key.permissions import HasAPIKey
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from project.api.app_employees.models import Employees, MyEndpoints
from project.utils.employee_utils import completeEmployeeInfo

import requests


# Create your views here.
class EmployeeInformation(APIView):
    """
         Autor: Gerardo Orellana
         Description:
                * GET:  get the employee information by id or all employees if id is not provided
                * POST: fill the employees from API consumption
    """
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [HasAPIKey, IsAuthenticated]

    def get(self, request):
        id = None
        if 'id' in request.data:
            id = request.data['id']
        try:
            if id:
                employees = Employees.objects.filter(id=id)
            else:
                employees = Employees.objects.all().order_by('id')
            results = []
            for employee in employees:
                results.append(completeEmployeeInfo(employee=employee))
            return Response(results, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(e, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request):
        my_endpoint = MyEndpoints.objects.filter(descriptor='employees')
        if len(my_endpoint) == 1:
            url = my_endpoint[0].api_id.dns_name + my_endpoint[0].path
            response = requests.get(url=url)
            if response.status_code == 200:
                Employees.objects.all().delete()
                for element in response.json():
                    employee = Employees()
                    employee.map(element)
                    employee.save()
            else:
                return Response({'data': {}, 'errors': [{'type': 'fatal',
                                                         'description': 'The MAS Global API did not response'}]},
                                status=status.HTTP_417_EXPECTATION_FAILED)
        else:
            return Response({'data': {}, 'errors': [{'type': 'fatal', 'description': 'There is no API configured'}]},
                            status=status.HTTP_417_EXPECTATION_FAILED)
