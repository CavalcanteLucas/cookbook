# Converting Strings into Datetimes

from datetime import datetime
text = '2012-09-20'
y = datetime.strptime(text, '%Y-%m-%d')
z = datetime.now()
y
z
diff = z - y
diff

z
nize_z = datetime.strftime(z, '%A %B %d, %Y')
nize_z

# Faster:
from datetime import datetime
def parse_ymd(s):
    year_s, mon_s, day_s = s.split('-')
    return datetime(int(year_s), int(mon_s), int(day_s))
