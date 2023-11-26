from datetime import datetime, date, timedelta

print(date.today())

duration = timedelta(days=2)

two_days_later = date.today() + duration
print(two_days_later)
print(duration.days)