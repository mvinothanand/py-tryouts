# Pydantic objects can be serialized to a dictionary
from pydantic_models import Employee

employee = Employee(
    name = 'MURUGAN',
    email = 'murugan@pazhani.com',
    date_of_birth = '1900-01-01',
    salary = 1234567.00,
    department= 'ENGINEERING',
    elected_benefits= False
)

employee_dict = employee.model_dump()
print(employee_dict)