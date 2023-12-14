nums = [1, 12, 42, 7, 9]
nums.reverse()
print(nums)

numscopy = nums.copy()
mynums = list(nums)
mycopy = nums[:]

print(numscopy)
print(mynums)

mycopy.sort()
print(mycopy)
print(nums)
print(type(nums))

# Tuples
mytuple = tuple(('Mucu', 15, False))
anothertuple = (7, 3, 1, 9)
print(mytuple)
print(type(anothertuple))
