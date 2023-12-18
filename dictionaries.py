band = {
    'vocals': 'planr',
    'guiter': 'page'
}

band2 = dict(vocal='planr', guiter='page')
print(band)
print(band2)
print(type(band))
print(type(band2))

# Accessing items in a dict
print(band['vocals'])
print(band.get('guiter'))
print(len(band2))

# list all keys
print(band.keys())
# list all values
print(band.values())

# List of key/values as tuples
print(band.items())

# change valurs in dict
band['vocals'] = 'sprono'
band.update({'bass': 'JPJ'})
print(band)

# Remove items
print(band.pop('bass'))
band['drums'] = 'machatte'
print(band)
print()
# delete and clear
band['drums'] = 'machatte'
del band['drums']
print(band)
band2.clear()
print(band2)
# del band2
print(band2)
print()

# copy dicts
# band2 = band - creates a reference
band2 = band.copy()
band2['drums'] = 'Mucu'
print(band2)

# use constructor func
band3 = dict(band)
print(band3)

# Nested dicts
member1 = {
    'Name': 'plant',
    'instrument': 'vocals'
}
member2 = {
    'Name': 'page',
    'instrument': 'guiter'
}
band = {
    'member1': member1,
    'member2': member2
}
print(band)
print(band['member1']['Name'])

# sets
nums = set((1, 2, 3, 4, 5))
print(nums)
print(type(nums))
print(len(nums))

# Add value to set
nums.add(9)
print(nums)
# add element from one set to anotheer
morenums = {6, 7, 8}
nums.update(morenums)
print(nums)

# print only dupes
one = {1, 2, 3}
two = {2, 3, 4, 5}
one.intersection_update(two)
print(one)
print()

one = {1, 2, 3}
two = {2, 3, 4, 5}
one.symmetric_difference_update(two)
print(one)
