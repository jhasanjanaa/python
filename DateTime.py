import datetime
print(datetime.datetime.now())

import time
print(time.strftime("%H:%M"))

specific_date = datetime(2025, 2, 15, 14, 30, 45)
print(specific_date)  # Output: 2025-02-15 14:30:45

# strptime() (string parse time) converts a string into a datetime object.
# strftime() (string format time) converts a datetime object into a formatted string.