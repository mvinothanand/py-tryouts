# Pydantic objects can be serialized to json strings

from pydantic_models import Employee
import json

employee = Employee(
    name = 'MURUGAN',
    email = 'murugan@pazhani.com',
    date_of_birth = '1900-01-01',
    salary = 1234567.00,
    department= 'ENGINEERING',
    elected_benefits= False
)

employee_json=employee.model_dump_json()
print(employee_json)

# Also, a JSON schema definition can be generated 
# A dictionary containing the schema details is generated
employee_json_schema = employee.model_json_schema()
print(employee_json_schema)

# Converts the json schema dict to json string
employee_json_schema_str = json.dumps(employee_json_schema)
print(employee_json_schema_str)