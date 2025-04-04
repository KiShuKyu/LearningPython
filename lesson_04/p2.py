# Movie Ticket Problem
import random

age = 20
days = ("Monday", "Wednesday", "Sunday")
day = random.choice(days)

print("Day:", day)

if age <= 18:
    price = 12
elif age >= 18:
    price = 12
if day == ("Wednesday"):
    print("There is a $2 Discount today")
    dis_price = price - 2
    print(f"Final Price: ${dis_price}")

else:
    print(f"Final Price: ${price}")
