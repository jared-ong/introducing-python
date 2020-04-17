# Basic while loop with a counter
count = 1
while count <= 5:
    print(count)
    count += 1

# Infinite loop with break statement
while True:
    stuff = input("string to capitalize [type q to quit]: ")
    if stuff == "q":
        break
    print(stuff.capitalize())

# Infinite loops with break on q or output square of even numbers
while True:
    value = input("Integer, please [q to quit]: ")
    if value == 'q':
        break
    number = int(value)
    if number % 2 == 0: # an even number
        continue
    print(number, "squared is", number*number)

# Loops with optional else condition
numbers = [1, 3, 5]
position = 0
while position < len(numbers):
    number = numbers[position]
    if number % 2 == 0:
        print('Found even number', number)
        break
    position += 1
else: #break not reached optional else condition
    print('No even number found')

# Iterate with for and in
# It's legal in python to step through a string in python like this
word = 'thud'
offset = 0
while offset < len(word):
    print(word[offset])
    offset += 1

# But there's a better pythonic way
for letter in word:
    print(letter)

# Cancel with break
word = 'thud'
for letter in word:
    if letter == 'u':
        break
    print(letter)

# Break use with else, if no break then will end with else
word = 'thud'
for letter in word:
    if letter == 'x':
        print("Eek! An 'x'!")
        break
    print(letter)
else:
    print("No 'x' in there'")


# generate number sequences with range(start,stop,step)
for x in range(0,3):
    print(x)

# Makes a list using range
print(list(range(0,5)))

# Make a range from 2 down to 0
for x in range(2, -1, -1):
    print(x)

print(list(range(0,11,2)))

