i = 0
while i < 10:
    print(i)
    i += 2

words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))

a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i])

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')
