from rest_framework_api_key.permissions import HasAPIKey
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from project.api.app_employees.models import Employees, MyEndpoints
from project.utils.employee_utils import completeEmployeeInfo

from drf_yasg.utils import swagger_auto_schema

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

    @swagger_auto_schema(
        operation_summary="Employee Data",
        operation_description="Service to get employee information",
        responses={200: 'List of employees',
                   500: 'There was a problem processing the request'}
    )
    def get(self, request):
        id = None
        if 'id' in request.data:
            id = request.data['id']
        try:
            if id:
                employees = Employees.objects.filter(id=id)
            else:
                employees = Employees.objects.all().order_by('id')
            results = [completeEmployeeInfo(employee=employee).serialize() for employee in employees]
            return Response(results, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(e, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @swagger_auto_schema(
        operation_summary="Employee Data API consumption",
        operation_description="Service to consume the MAS Global consulting API and send it to a table in sqlite",
        responses={200: 'Operation Result',
                   417: 'Expectation Failed'}
    )
    def post(self, request):
        my_endpoint = MyEndpoints.objects.filter(descriptor='employees')
        if len(my_endpoint) == 1:
            url = my_endpoint[0].api_id.dns_name + my_endpoint[0].path
            response = requests.get(url=url)
            if response.status_code == 200:
                Employees.objects.all().delete()
                records = 0
                bad_records = 0
                for element in response.json():
                    try:
                        employee = Employees()
                        employee.map(element)
                        employee.save()
                        records += 1
                    except Exception: #FIXME too general exception, running short on time
                        bad_records += 1
                return Response({'data': {'records_ok': records, 'records_bad': bad_records,
                                          'status': 'Happy place' if bad_records == 0 else 'Not such a happy place'}},
                                status=status.HTTP_200_OK)
            else:
                return Response({'data': {}, 'errors': [{'type': 'fatal',
                                                         'description': 'The MAS Global API did not response'}]},
                                status=status.HTTP_417_EXPECTATION_FAILED)
        else:
            return Response({'data': {}, 'errors': [{'type': 'fatal', 'description': 'There is no API configured'}]},
                            status=status.HTTP_417_EXPECTATION_FAILED)
