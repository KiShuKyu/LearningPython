# Function with args
def sum_all(*args):
    print(args)
    for i in args:  # i takes each value one by one in each loop
        print(i * 2)
    return sum(args)


print(sum_all(1, 2, 3))
# print(sum_all(1, 2, 3, 4, 5))
# print(sum_all(1, 2, 3, 4, 5, 6, 7, 8))
