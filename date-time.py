from datetime import datetime, date, timedelta

# Today's date
print(date.today())

# Using Time Delta
duration = timedelta(days=2)

two_days_later = date.today() + duration
print(two_days_later)
print(duration.days)

# Convert string to date object
date_as_str = "2024-May-20"
date_as_obj = datetime.strptime(date_as_str, "%Y-%b-%d")
print(f'date as obj: {date_as_obj}')