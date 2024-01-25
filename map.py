my_list = [2,3,4]

def mult_by2(i):
    return i * 2

def only_odd(i):
    return i % 2 != 0

print(my_list)
print(list(filter(only_odd, my_list)))
print(list(map(mult_by2, my_list)))
