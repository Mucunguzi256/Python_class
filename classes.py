class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def moves(self):
        print('Moves Along...')

    def get_make_model(self):
        print(f"I'm a {self.make} {self.model}.")


my_car = Vehicle('Toyota', 'MarkX')
# print(my_car.make)
# print(my_car.model)
my_car.get_make_model()
my_car.moves()
print()
your_car = Vehicle('Mitshubish', 'Escoodo')
your_car.get_make_model()
print()


class Airplane(Vehicle):
    def __init__(self, make, model, faa_id):
        super().__init__(make, model)
        self.faa_id = faa_id

    def moves(self):
        print('Flies Along...')


class Truck(Vehicle):

    def moves(self):
        print('Rambles Along...')


class Golfcart(Vehicle):
    pass


cessna = Airplane('Cessna', 'Skyhawk', 'UG-25617')
benz = Truck('Benz', 'Mercedes')
golfwagon = Golfcart('Yamaha', 'GC100')

cessna.get_make_model()
cessna.moves()
benz.get_make_model()
benz.moves()
golfwagon.get_make_model()
golfwagon.moves()

print('\n\n\n\n')

for v in (my_car, your_car, cessna, benz, golfwagon):
    v.get_make_model()
    v.moves()
