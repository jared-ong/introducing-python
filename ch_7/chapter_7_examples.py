# Define Tuple
empty_tuple = ()
a = (7,2)
b = (7,2,9)
c = (7,4,9)

# Compare lists
a < b
a < c
b < c
d = (7,5,9)
d < c
c < d
id(d)



# Define list, good for keeping track of ordered items
empty_list = []
lista = [1,2,3,4,10]
id(lista)
lista = [1,2,3,4,20]
id(lista)

# Convert a tuple to list
names = ("John", "Jerry", "Bob")
names_list = list(names)
type(names)
type(names_list)

# Create a list from string using split function
directory = 'C:\\users\\bonkers\\filename.csv'
path_split = directory.split('\\')
path_split

# Get items by offset
path_split[0]
filename = path_split[len(path_split) - 1]

# Add items to end of a list by using append
names_list = list(names)
names_list.append("Jimmy")
names_list

# Add an item in a specific order in the list by using insert with offset
names_list.insert(2,"Wally")
names_list

# Combine lists by using extend() function or plus function
names2 = ["Johnny","Wilbur"]
names_list.extend(names2)
names_list

names3 = ["Matthew","Mark","Luke","John"]
names_list += names3
names_list

# Change an item by [offset]
names_list[2] = 'Wanda'
names_list

# Delete an item by value with remove(), if duplicate items, remove only deletes the first one
names_list.remove("Jimmy")

# Iterate through list
for name in names_list:
    print(name)

# Delete all items with clear()
names2.clear()
names2

# Find an item's offset by value with index()
names_list.index("Wanda")

# Test for value in list
if "Wanda" in names_list:
    print("We have a Wanda")

# Count occurrences of a value
lots_of_lukes = ["Luke","Luke","Luke"]
names_list.extend(lots_of_lukes)
names_list.count("Luke")

# Sort and sorted to sort a list
names_list2 = sorted(names_list)
names_list # Didn't change the list
# Sort, sorts the list in place
names_list.sort()
names_list


# When you assign one list to more than one variable
# changing the list in one place also changes the other
a = [1,2,3]
b = a
a[0] = "surprise"
print(a)
print(b)
id(a)
id(b)

# Copy everything with deep copy

a = [1, 2, [8, 9]]
b = a.copy()
c = list(a)
d = a[:]
print(a)
print(b)
print(c)
print(d)
a[2][1] = 10
print(a)
print(b)
print(c)
print(d)
a[1] = 5
print(a)
print(b)
print(c)
print(d)


# All methods of copying from one list to another were "shallow"
import copy
a = [1, 2, [8, 9]]
b = copy.deepcopy(a)
print(a)
print(b)

# Copy to a new list using copy(), list(), or a slice
c = a.copy()
id(c)


# Zip function - iterates over multiple lists in parallel
days = ['Monday','Tuesday','Wednesday']
fruits = ['banana','orange','peach']
drinks = ['beer','milk','juice']
days_fruits = zip(days,fruits,drinks)
print(days_fruits)
for day, fruit, drink in days_fruits:
    print("On ", day, " eat a ", fruit, " and drink a ", drink)

# List of lists
days_eat_list = [days, fruits, drinks]
print(days_eat_list)

# You can do nested loops in python
for list in days_eat_list:
    for item in list:
        print(item)

