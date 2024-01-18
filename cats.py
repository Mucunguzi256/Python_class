#OOP

class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age

black_cat = Cat('Bongo', 2)
white_cat = Cat('Maa', 4)
indie_cat = Cat('Pala', 7)

def oldest_cat(*args):
    return max(args)



print(f"The oldest cat is {oldest_cat(black_cat.age, white_cat.age, indie_cat.age)} years old.")
