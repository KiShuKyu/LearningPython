# prime number checker

number = 13

is_prime = True

if number > 1:
    for i in range(2, number):
        if (number % i) == 0:  # If number is divisible by i with no remainder
            is_prime = False
            break

print(is_prime)
