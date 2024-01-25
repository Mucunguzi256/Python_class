# Map, Filter, Zip and Reduce

# import reduce
from functools import reduce

my_list = [2,3,4]
your_list = [5,7,9]
def mult_by2(i):
    return i * 2

def only_odd(i):
    return i % 2 != 0

def accumulator(acc, i):
    return acc + i


print((reduce(accumulator, my_list, 0)))
print(list(zip(your_list, my_list)))
print(list(filter(only_odd, my_list)))
print(list(map(mult_by2, my_list)))
