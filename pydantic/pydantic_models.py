from datetime import date
from uuid import UUID, uuid4
from enum import Enum
from pydantic import BaseModel, EmailStr

class Department(Enum):
    HR = 'HR'
    SALES = 'SALES'
    IT= 'IT'
    ENGG = 'ENGINEERING'


class Employee(BaseModel):
    name: str
    # Type UUID. creates a default uuid
    employee_id: UUID = uuid4()
    email: EmailStr
    date_of_birth: date
    salary: float
    department: Department
    elected_benefits: bool


# employee successfully created with valid data for all fields
# Note: employee_id will be created during instantiation
employee_valid = Employee(
    name = 'MURUGAN',
    email = 'murugan@pazhani.com',
    date_of_birth = '1900-01-01',
    salary = 1234567.00,
    department= 'ENGINEERING',
    elected_benefits= False
)

# print(employee_valid)


# Below is an attempt to create an employee object with invalid data
# Throws a ValidationError with details
# employee_invalid = Employee(
#     name = 123,
#     employee_id = 123,
#     email = 'murugan#pazhani.com',
#     date_of_birth = '1900-01-AB',
#     salary = 'ABCD',
#     department= 'ENGI',
#     elected_benefits= False 
# )


