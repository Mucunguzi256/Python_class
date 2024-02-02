def generator_fn(n):
    for i in range(n):
        yield i * 2

g = generator_fn(10)
next(g)
next(g)
next(g)
print(next(g))

def fib(num):
    a = 0
    b = 1
    for i in range(num):
        yield a
        temp = a
        a = b
        b = a + b

for x in fib(21):
    print(x)
