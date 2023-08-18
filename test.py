#def availability_superimposition():

def dummy(*args):
  for arg in args:
    print(arg)


def get_merged_bitmap(staff_records):
  staff_all_days_merged_bm = []
  for i in range(5):
    staff_day_bm = []
    for staff in staff_records:
      staff_day_bm.append(staff["avail_bitmap"][i])
    staff_day_merged_bm = merged_bitmap(staff_day_bm)
    print(f"day {i + 1} merged bm: {staff_day_merged_bm}")
    staff_all_days_merged_bm.append(staff_day_merged_bm)
  return staff_all_days_merged_bm

def merged_bitmap(input_list):
  day_merged_bm = ""
  for i in range(8):
    result = 0
    for item in input_list:
      result += int(item[i])
    #print(f"{i} {result}")
    day_merged_bm = str(day_merged_bm) + str("0" if result == 0 else "1")
    #print(day_merged_bm)
  return day_merged_bm


def update_staff_details(in_staff_details):
  for staff in staff_details:
    staff["exp"] = 2

mylist = ["01000000","00101000","00000111"]

staff_details = [
  {
    "name": "staff-1",
    "avail_bitmap": ["00100000", "10000000","00000000","00000100","00000000"]
  },
  {
    "name": "staff-2",
    "avail_bitmap": ["00001000", "00000000","11001000","00000110","00000000"]
  },
  {
    "name": "staff-3",
    "avail_bitmap": ["00000111", "00000000","11000100","00000010","00000000"]
  }
]

#dummy(*["00000000","00000000","00000000"])
#print(merged_bitmap(mylist))
#print(get_merged_bitmap(staff_details))
update_staff_details(staff_details)
print(staff_details)