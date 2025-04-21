# To find a square of a number

def square(number):  # () parameters
    return number ** 2  # why we didnt use print is because print value hold nhi krta and return ne usse result me hold karvaya


number = int(input("Enter the number you want the Square of:\n"))
result = square(number)
print(f"The Square of the number {number} is:- {result}.")
