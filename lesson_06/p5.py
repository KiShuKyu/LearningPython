# Default Parameter Value

# name = input("Enter Your name here:\n")


def greet(name="User"):
    return "Hellow ," + name + "!"


print(greet("name"))
print(greet())
