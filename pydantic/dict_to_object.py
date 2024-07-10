from pydantic_models import Employee

# Pydantic allows to convert a dictionary into an object directly
# given the keys and values follow the data schema defined in the
# pydantic model of the class
new_employee_dict = {
    'name': 'GANESHA',
    'email': 'ganesha@pillaiyarpatti.com',
    'date_of_birth': '2000-01-01',
    'salary': 1234567.00,
    'department': 'IT',
    'elected_benefits': False
}

new_employee = Employee.model_validate(new_employee_dict)
print(new_employee)