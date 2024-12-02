from time import time, gmtime
from datetime import datetime

current_time = time() # returns Epoche time
print('Seconds since January 1, 1970: ', current_time, ' or ', "%.2e" % current_time, ' in scientific notation')

gmt_time = gmtime(current_time)
# help(gmtime)
formatted_gmt = datetime(gmt_time.tm_year, gmt_time.tm_mon, gmt_time.tm_mday)

print(formatted_gmt.strftime("%B %d %Y"))
