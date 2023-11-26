# Reference: https://docs.python.org/3/howto/enum.html?highlight=enum
from enum import Enum
from enum import Flag
from datetime import date

# Basic Enum definition
class Colours(Enum):
  RED = 1
  BLUE = 2
  GREEN = 3

#Accessing a Enum defined value
print(Colours.RED.value)

# Enums allow to write added functionality
# In the below example, a classmethod decorated function is attached to return the isoweekday
class weekday(Enum):
  MONDAY = 1
  TUESDAY = 2
  WEDNESDAY = 3
  THURSDAY = 4
  FRIDAY = 5
  SATURDAY = 6
  SUNDAY = 7
  @classmethod
  def get_today(cls, date: date):
    return cls(date.isoweekday())

print(weekday.get_today(date.today()).value)

#Flags - use this type of enum if you dont want to use list for values


