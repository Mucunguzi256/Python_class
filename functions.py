def hello():
    print('Hi reader!')


hello()


# def sum(num1, num2):
#     return num1 + num2


# total = sum(6, 7)
# print(total)

def sum(num1=0, num2=0):
    if (type(num1) is not int or type(num2) is not int):
        return 0
    return num1 + num2


total = sum(5, 7)
print(total)


def multiple_items(*args):
    print(args)
    print(type(args))


multiple_items()


def mult_named_items(**kwargs):
    print(kwargs)


mult_named_items(first='Mucu', second='Moe')
