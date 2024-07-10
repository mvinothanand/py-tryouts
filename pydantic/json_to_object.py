# JSON strings that confine to a Pydantic model class
# can be converted to an object
from pydantic_models import Employee

employee_json_string = """
{"employee_id":"d2e7b773-926b-49df-939a-5e98cbb9c9eb",
"name":"SHIVA",
"email":"shiva@kailasa.com",
"salary":123456.50,
"date_of_birth":"1900-01-01",
"department":"HR",
"elected_benefits":false
}
"""

employee_json=Employee.model_validate_json(employee_json_string)
print(employee_json)