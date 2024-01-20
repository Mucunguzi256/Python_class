# Strings

# String Literal
import math
first = 'Mucu'
last = 'Moe'

# print(type(last))
# print(type(last) == str)
# print(isinstance(last, str))

# constructor function
# pizza = str('Pepperoni')
# print(type(pizza))
# print(type(pizza) == str)
# print(isinstance(pizza, str))

# concatnation
fullName = first + ' ' + last
print(fullName)
fullName += '!'
print(fullName)

# Casting num to str
decade = str(1980)
print(type(decade))
print(decade)

statement = 'I was born in' + ' ' + decade + 's.'
print(statement)

# multip[le line
multiline = '''
Hey, How are you

I was just checking in.

            All g?

'''
print(multiline)

# escaping special characters
sentance = 'I\'am back at work!\tHey!\n\n Where\'s this at\\ located?'
print(sentance)

# String methods
print(first)
print(first.lower())
print(first.upper())
print(multiline.title())
print(multiline.replace('g', 'ok'))
print(len(multiline))

print('')

# Build menu

title = 'menu'.upper()
print(title.center(20, '='))
print('Coffee'.ljust(16, '_') + '1$'.rjust(5))
print('Maffin'.ljust(16, '_') + '2$'.rjust(5))
print('Chappati'.ljust(16, '_') + '1.5$'.rjust(5))
print('Cheesecake'.ljust(16, '_') + '3$'.rjust(5))

print('')
# string index values
print(first[1])
print(first[1:-1])
print(first[1:])
print('')

# some methods return boolean values
print(first.startswith('M'))
print(first.endswith('a'))
# print(first.startswith('M'))
print('')

# Numeric data types
# comp value

compValue = 5+7j
print(type(compValue))
print(compValue.real)
print(compValue.imag)

# Bultin funcs for nums
abc = 1.46
print(abs(abc))
print(round(abc))
print(round(abc, 1))

print(math.pi)
print(math.sqrt(25))
print(math.ceil(abc))
print(math.floor(abc))

# casting string to number
zipcode = '10002'
zipValue = int(zipcode)
print(type(zipValue))
