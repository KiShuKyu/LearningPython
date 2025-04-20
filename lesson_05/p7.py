# Valid input (imp)

while True:
    number = int(input("Enter value between 1 and 10:\n "))
    if 1 <= number <= 10:
        square = number * number
        print(
            f"Your number is:{number} and square of that number is {square}.")
        break
    else:
        print("You must enter a valid number.")
