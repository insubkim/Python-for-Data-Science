from time import time, gmtime
from datetime import datetime

current_time = time() # returns Epoche time
print('Seconds since January 1, 1970: ', current_time)
gmt_time = gmtime(current_time) # parses to year mon day min sec etc
print(gmt_time)
formatted_gmt = datetime(gmt_time.tm_year, gmt_time.tm_mon, gmt_time.tm_mon) # something useful?
print(formatted_gmt)
print(formatted_gmt.strftime("%B"))
