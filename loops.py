# value = 1
# while value < 10:
#     print(value)
#     if value == 6:
#         break
#     value += 1

# value = 1
# while value <= 10:
#     value += 1
#     if value == 6:
#         continue
#     print(value)
# else:
#     print('The value is now equal to ' + str(value))

names = ['Joe', 'Mucu', 'Dave']
# for x in names:
#     print(x)
for x in range(0, 100, 5):
    print(x)

actions = ['eats', 'sleeps', 'dances']

for name in names:
    for action in actions:
        print(name + ' ' + action + '.')
for action in actions:
    for name in names:
        print(name + ' ' + action + '.')
