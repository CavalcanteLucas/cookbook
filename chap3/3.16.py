# Manipulating Dates Involving Time Zones

from datetime import datetime, timedelta
from pytz import timezone, utc

d = datetime(2012, 12, 21, 9, 30, 0)
print(d)


# Localize the date for Chicaco
central = timezone('US/Central')

loc_d = central.localize(d)
print(loc_d)

# Convert to Bangalore time
bang_d = loc_d.astimezone(timezone('Asia/Kolkata'))
print(bang_d)

d = datetime(2013, 3, 10, 1, 45)
loc_d = central.localize(d)
print(loc_d)
later = loc_d + timedelta(minutes=30)
print(later)


# Discussion

print(loc_d)
utc_d = loc_d.astimezone(utc)
print(utc_d)