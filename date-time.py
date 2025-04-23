from datetime import datetime, date, timedelta, timezone, time
from zoneinfo import ZoneInfo


# # Today's date
# print(date.today())

# # Using Time Delta
# duration = timedelta(days=2)

# two_days_later = date.today() + duration
# print(two_days_later)
# print(duration.days)

# # Convert string to date object
# date_as_str = "2024-May-20"
# date_as_obj = datetime.strptime(date_as_str, "%Y-%b-%d")
# print(f'date as obj: {date_as_obj}')

# # TIMEZONES
# # default provides the current time in the local system's timezone
# # however will not have any timezone information attached to the datetime obj
# now_in_local_sys_time_wo_tzinfo = datetime.now()
# print(f'Current time in local system time: {now_in_local_sys_time_wo_tzinfo}, Timezone: {now_in_local_sys_time_wo_tzinfo.tzinfo}') 


# now_in_local_sys_time_with_tzinfo = datetime.now(tz=timezone.utc)
# print(f'Current time in UTC: {datetime.now(tz=timezone.utc)}, Timezone: {now_in_local_sys_time_with_tzinfo.tzinfo}')

# # get the current time in IST
# # set the ist offset from UTC: +5:30
# ist_offset = timezone(timedelta(hours=5, minutes=30))
# now_in_ist = datetime.now(ist_offset)
# print(f'Current time in IST: {now_in_ist}, Timezone: {now_in_ist.tzinfo}')

# # the timezone class of the datetime package is not convenient working with
# # different timezones and when daylight savings and all come into picture.
# # So using pytz or dateutil libraries shall be used to handle tz. They have
# # Python 3.9 and above have zoneinfo module included in the standard library.
# # The zoneinfo module uses the IANA (Internet Assigned Numbers Authority)'s Timezone database
# #  which is upto date about the changes in day light savings etc.


# # get the current time in IST using the zoneinfo module
# now_in_ist_using_zoneinfo = datetime.now(ZoneInfo("Asia/Kolkata")) # the timezone string is as per IANA database
# print(f'Current time in IST using zoneinfo module: {now_in_ist_using_zoneinfo}, Timezone: {now_in_ist_using_zoneinfo.tzinfo}')

# # get the current time in UTC using the zoneinfo module
# now_in_utc_using_zoneinfo = datetime.now(ZoneInfo("UTC"))
# print(f'Current time in UTC using zoneinfo module: {now_in_utc_using_zoneinfo}, Timezone: {now_in_utc_using_zoneinfo.tzinfo}')


# Create a datetime with hours, minuts and seconds set to zero
today = date.today()
time_component = time(hour=23, minute=59, second=59, tzinfo=ZoneInfo("Asia/Kolkata"))
full_datetime = datetime.combine(today, time_component)
print(full_datetime)


