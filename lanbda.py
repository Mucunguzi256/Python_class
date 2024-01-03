

from functools import reduce
def sqrd(num): return num * num
# lambda num : num * num


print(sqrd(2))


def sum_total(a, b): return a + b


print(sum_total(7, 9))
###########
print()


def funcbuilder(x):
    return lambda num: num + x


add_ten = funcbuilder(10)
add_twenty = funcbuilder(20)

print(add_ten(9))
print(add_twenty(7))

######
print()

nums = [2, 4, 7, 9, 25]
sqrd_nums = map(lambda num: num * num, nums)
print(list(sqrd_nums))

print()


odd_nums = filter(lambda num: num % 2 != 0, nums)
print(list(odd_nums))


nums = [1, 2, 3, 4, 5, 1]
total = reduce(lambda acc, curr: acc + curr, nums)
print(total)
print(sum(nums))

# lambda acc, curr: acc + len(curr)
names = ['Mucu', 'Debbie', 'Zolla']
char_count = reduce(lambda acc, curr: acc + len(curr), names, 0)
print(char_count)
