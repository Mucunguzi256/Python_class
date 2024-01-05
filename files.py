import os






# R -read
# A -append/update
# W -write
# X -create

# Read - error if it doesn't exist

f = open('names.txt')
#print(f.read())
#print(f.read(4))
# print(f.readline())
# print(f.readline())

for line in f:
    print(line)

f.close()

try:
    f = open('named_list.txt')
    print(f.read())
except:
    print("File you're looking for doesn't exist")
finally:
    f.close()

# A append creates file if it doesn't exist

f = open('names.txt', 'a')
f.write('Mucu')
f.close()

f = open('names.txt')
print(f.read())
f.close()

# Write (overwrite)
f = open('content.txt', 'w')
f.write('I deleted all of content')
f.close()

f = open('content.txt')
print(f.read())
f.close()

# creating a new file (two ways)

# opening file for writing, als creates file if it doesn't exist

f = open('named_list.txt', 'w')
f.close()


# creates specied file but returns an error if file exists

if not os.path.exists('mucu.txt'):
    f = open('mucu.txt', 'x')
    f.close()

# deleve file
# avoid error if it doesn't exist
if os.path.exists('mucu.txt'):
    os.remove('mucu.txt')
else:
    print("File you're trying to delete doesn't exist")


# "with" key word
with open("named_list.txt") as f:
    content = f.read()

with open("names.txt", 'w') as f:
    f.write(content)
