x = 99  # global


def f1():
    x = 88

    def f2():
        print(x)
    return f2


myResult = f1()
myResult()


# Second (closur)
def coder(num):
    def actual(x):
        return x ** num
    return actual


f = coder(2)
g = coder(3)

print(f(3))
print(g(3))
