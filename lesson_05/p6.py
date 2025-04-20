# Factorial

number = 5
original_number = 5
factorial = 1

while number > 0:
    factorial = factorial * number
    number = number - 1

print(
    f"The factorial value of the given number:{original_number} is {factorial}.")
