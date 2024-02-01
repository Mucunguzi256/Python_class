def generator_fn(n):
    for i in range(n):
        yield i * 2

g = generator_fn(10)
next(g)
next(g)
next(g)
print(next(g))
