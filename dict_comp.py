simple_dict = {
    'a': 2,
    'b': 3,
    'c': 4
}

my_dict = {key:value**2 for key,value in simple_dict.items()}

print(my_dict)
