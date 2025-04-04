# Leap year checker

year = 2025

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print(year, " is a leep year.")
else:
    print(year, "is not a leap year.")
