from datetime import datetime

# Get the current day, month, year, hour, minute and timestamp from datetime module

now = datetime.now()
print(f"{now.day}.{now.month}.{now.year} {now.hour}:{now.minute} {now.timestamp()}")

# Format the current date using this format: "%m/%d/%Y, %H:%M:%S")

now_format = now.strftime("%m/%d/%Y, %H:%M:%S")
print(now_format)

# Today is 5 December, 2019. Change this time string to time.

date_str = "Today is 5 December, 2019"
date_str_format = datetime.strptime(date_str, "Today is %d %B, %Y")
print(date_str_format)

# Calculate the time difference between now and new year.

new_year = datetime(2024, 1, 1)
print("Time left for new year: ", new_year - now)

# Calculate the time difference between 1 January 1970 and now.

old_date = datetime(1970, 1, 1)
print("Time left: ", now - old_date)