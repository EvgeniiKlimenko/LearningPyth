import datetime

utc_time = datetime.datetime.now(datetime.UTC)
print(utc_time)

now_time = datetime.datetime.now()
print(now_time.isoformat())
print(now_time.date())  # extract date from datetime

print(now_time.year)
print(now_time.day)
print(now_time.weekday())

my_date = datetime.datetime(year=2045, month=5, day=2, hour=12, minute=30)
print(f"My selfmade date: {my_date}")

current_date = datetime.date.today()
print(f"Only date: {current_date}")

days_ago = current_date - datetime.timedelta(days=5)  # go back and forth on timeline
print(f"Day ago: {days_ago}")

# pretty printing with regexp
print(f"Formatted print: {now_time.strftime("%A, %d %B %Y")}")

# create datetime obj from string:
iso_format = "2024-03-13T12:33:14.465861"
date_time_convert = datetime.datetime.fromisoformat(iso_format)
print(type(date_time_convert))
