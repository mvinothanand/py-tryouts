my_list_of_dicts = [
  {
    "name": "vinoth",
    "password": "pass"
  },
  {
    "name": "senthil",
    "password": "pass"
  }
]

print(my_list_of_dicts)

for item in my_list_of_dicts:
  if item["name"] == "vinoth":
    item["status"] = True

print(my_list_of_dicts)