# Classify a person's age group
import math

key = ("Child", "Teenager", "Adult", "Senior")

age = 100
age_in = int(age)
# find_age = input("What is your age?")
# find_age_in = int(find_age)
# print(find_age)

if age <= 13:
    print(age, "Child")
elif age <= 19:
    print(age, "Teenager")
elif age <= 59:
    print(age, "Adult")
elif age <= 1000:
    print(age, "Senior")
else:
    age not in age
    print("You must enter a valid number")
# return find_age()
