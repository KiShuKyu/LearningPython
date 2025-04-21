# generate a function with Yield
def even_generator(limit):
    for i in range(2, limit + 1, 2):
        yield i  # ye bhi value return krta h lekin value memory me stor krta h kaha pr tha


for num in even_generator(10):
    print(num)


# 2	((Start at 2 (the first even number)
# limit + 1	(Go up to limit (we add +1 because range() stops before limit))
# 2 (step)	(Count by 2s (so we only get even numbers))
