from datetime import date
from uuid import UUID, uuid4
from enum import Enum
from pydantic import BaseModel, EmailStr, Field

class Department(Enum):
    HR = 'HR'
    SALES = 'SALES'
    IT= 'IT'
    ENGG = 'ENGINEERING'


# Field Attributes:
# default_factory: specify a callable that is ought to give a default value
# frozen: make a field immutable. value can't be changed after instantiation.
# min_length: specify a minimum length for a string variable
# pattern: specify a regex pattern validation for a string variable
# alias: specify alias names that will be used during
#    instantiation or serialization of the pydantic object
# repr: should the attribute be included in the string
#    representation of the object
# gt: boundary for an integer attribute

class Employee(BaseModel):
    name: str = Field(min_length=1, frozen=True)
    # Type UUID. creates a default uuid
    employee_id: UUID = Field(default_factory=uuid4, frozen=True)
    #email: EmailStr = Field(pattern=r".+@tci\.com$")
    email: EmailStr
    date_of_birth: date = Field(alias='birth_date', repr=True, frozen=True)
    salary: float = Field(alias='compensation', gt=0, repr=True)
    department: Department
    elected_benefits: bool


# Create a new employee
# errors as per the validations defined
# new_employee = Employee(
#     name='',
#     # throws an error as the domain doesn't match with the given pattern
#     email='kannappan@example.com',
#     birth_date='2020-10-10',
#     compensation=1000,
#     department='HR',
#     elected_benefits=True
# )

new_employee = Employee(
    name='a',
    # throws an error as the domain doesn't match with the given pattern
    email='kannappan@tci.com',
    # this field will be mapped to date_of_birth
    birth_date='2020-10-10',
    # this field will be mapped to salary
    compensation=1000,
    department='HR',
    elected_benefits=True
)

# print(new_employee)

# Covert a dict to employee
dict_employee = {
    'name': 'a',
    'email': 'kannappan@tci.com',
    'birth_date': '2020-10-10',
    'compensation': 1000,
    'department': 'HR',
    'elected_benefits': True
}

dict_emp_obj = Employee.model_validate(dict_employee)
print(dict_emp_obj)