# Sum of even numbers up to given num "n"

n = 10
sum_number_count = 0

for num in range(1, n+1):
    if n % 2 == 0:
        sum_number_count += 1
print("The Sum of total even numbers is", sum_number_count)
