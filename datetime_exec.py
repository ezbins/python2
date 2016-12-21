#!/usr/bin/env python3

import datetime as dt


today = dt.datetime.now()
year = today.year
month = today.month
day = today.day

weekday = dt.datetime.now().weekday()

print(weekday)
print(today)
print(year)
print(month)
print(day)