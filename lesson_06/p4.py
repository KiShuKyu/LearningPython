# Function returning multiple values
import math

radius = int(input("Enter the Radius:\n"))


def formula(radius):
    area = 3.14 * (radius ** 2)
    circumference = 3.14 * 2 * radius
    return area, circumference


a, c = formula(3)
print("Area:", a, " Circumference:", c)

# area = str(input("Area\n"))  # pi r ** 2
# # if Area == Area
# circumference = str(input("Circumference"))  # 2 pi r
