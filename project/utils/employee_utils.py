
def completeEmployeeInfo(employee):
    if employee.contract_type_name == 'HourlySalaryEmployee':
        employee.annual_salary = 120 * employee.hourly_salary * 12
    elif employee.contract_type_name == 'MonthlySalaryEmployee':
        employee.annual_salary = employee.monthly_salary * 12

    return employee
