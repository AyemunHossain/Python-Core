#;==========================================
#; Title:  Customize the time 
#; Author: @AyemunHossain
#;==========================================


from datetime import datetime
import time

now = time.time()
print(now)

#if you want time like : 2020-01-20 20:54:29.243630 then
print(datetime.fromtimestamp(now))

#if you want time like : 2020-01-20 20:54:29 then
print(datetime.strftime(datetime.fromtimestamp(now), '%Y-%m-%d %H:%M:%S'))

#.............Actually you can customize any format you want :
print(datetime.strftime(datetime.fromtimestamp(now), '%Y-%m-%d'))
print(datetime.strftime(datetime.fromtimestamp(now), '%d-%m-%Y'))
print(datetime.strftime(datetime.fromtimestamp(now), '%d-%m-%y'))