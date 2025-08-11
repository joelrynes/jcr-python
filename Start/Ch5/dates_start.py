#
# Example file for working with date information
# LinkedIn Learning Python course by Joe Marini
#


from datetime import date
from datetime import datetime

## DATE OBJECTS
# Get today's date from the simple today() method from the date class
dt=date.today()
print(f"today date is: {dt}")

# print out the date's individual components
print(dt.day, dt.year, dt.month)

# retrieve today's weekday (0=Monday, 6=Sunday)


## DATETIME OBJECTS
# Get today's date from the datetime class
dtt=datetime.now()
print(f"time now is: {dtt}")
# Get the current time
print(datetime.time(dtt))