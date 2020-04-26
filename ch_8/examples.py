# Dictionary like lists but with key:value pairs
empty_dict = {}

# Colon separates keys:values and a comma separates between each key:value
# Key is often a string but can be any of Python's immutable types: boolean, integer, float, tuple, string, and others
my_dictionary = {"Drug":"Penicillin",
                 "Side Effects":["Nausea", "Headache", "Dizziness", "Vomiting"],
                 "Dosage":500,
                 "Max Dosage":5000,
                 "Min Dosage":0,
                 "Treatment":"Good for all sorts of Bacterial infections"}
print(my_dictionary)

# Can define a dictionary using dict() function and passing named arguments

# Can convert two-value sequences into a dictionary with dict
# list of two-item tuples
lot = [('a','b'), ('c','d'), ('e','f')]
vals = dict(lot)
print(vals)

# tuple of two-item lists
tol = (['a','b'], ['c','d'], ['e','f'])
vals = dict(tol)
print(vals)

# list of two-char strings
los = ['ab', 'cd', 'ef']
vals = dict(los)
print(vals)

# tuple of two-char strings
tos = ('ab', 'cd', 'ef')
vals = dict(tos)
print(vals)

# Add a new key value pair.  
my_dictionary["Frequency Given"] = "Daily"
# Update a value by key. Remember all keys must be unique so if it exists it will update.
my_dictionary["Drug"] = "Advil"
print(my_dictionary)


# Get an item by [key] or with get()
print("Dosage is:", my_dictionary["Dosage"])

# If key is not present you will get an exception
# print(my_dictionary["Trial"])

# Two ways to avoid this error use an if condition to check if key exists before referencing
if "Trial" in my_dictionary:
    print("Key exists")

# Alternatively use the get() function, second argument is used if the Key doesn't exist
vara = my_dictionary.get("Trial", "No Trial Exists")
print(vara)
# Otherwise you will get None if second argument is not used
vara = my_dictionary.get("Trial")
print(vara)

# Use the keys() function to list all keys in a dictionary
the_keys = my_dictionary.keys()
type(the_keys)

# To convert dict_keys object to a list simply use list() function
keys_list = list(the_keys)
type(keys_list)

# Use the values() function to get the values of the dictionary without keys
the_vals = my_dictionary.values()
type(the_vals)

# Convert to list
vals_list = list(the_vals)
type(vals_list)

# Use the item() function to return the key/value pairs as a list of tuple
the_items = my_dictionary.items()
type(the_items)

# Convert to list of tuples
items_list = list(the_items)
print(items_list)

# Count your key value pairs
how_many = len(my_dictionary)
print(how_many)

# Combine dictionaries with update(), if duplicate keys exist the second dict wins
# Also notice the use of dictionary of dictionaries
dict1 = {"Member1": {"First Name": "John", "Last Name": "Doe"},
         "Member2": {"First Name": "James", "Last Name": "Kennedy"}}

dict2 = {"Member2": {"First Name": "Nolan", "Last Name": "Ryan"},
         "Member3": {"First Name": "Random", "Last Name": "Guy"},
         "Member4": {"First Name": "Jenny", "Last Name": "Jones"}}

dict1.update(dict2)
print(dict1)

# Delete an item by key
del dict1["Member4"]

# Dictionary comprehensions
# Format like this {key_expression: value_expression for expression in iterable}
word = "letters"
letter_counts = {letter: word.count(letter) for letter in word}
letter_counts

# Sets https://www.geeksforgeeks.org/sets-in-python/
# Sets in Python
# A Set is an unordered collection data type that is iterable,
# mutable and has no duplicate elements. Python’s set class represents the
# mathematical notion of a set. The major advantage of using a set,
# as opposed to a list, is that it has a highly optimized method for
# checking whether a specific element is contained in the set.
# This is based on a data structure known as a hash table.
# Since sets are unordered, we cannot access items using indexes
# like we do in lists.

empty_set = set()
even_numbers = {0,2,4,6,8}
odd_numbers = {1,3,5,7,9}
# Get length with len()
len(odd_numbers)

# Add and item with add()
odd_numbers.add(11)
print(odd_numbers)

# Remove an item by value remove()
odd_numbers.remove(3)
print(odd_numbers)
set1 = {"Joe","John","Jeff","Sally","Sue"}
set2 = {"John","Sue","Wally","Bob","Jane"}

# Intersection operator, similar to inner joinn
print(set1 & set2)
print(set1.intersection(set2))

# Union (members of each set)
print(set1 | set2)
print(set1.union(set2))

# Difference between the two sets
print(set1 ^ set2)
print(set1.symmetric_difference(set2))

# Set comprehension
# Format like {expression for expression in iterable}
# It can have the optional condition tests {expression for expression in iterable if condition}
a_set = {number for number in range(1,6) if number % 3 == 1}
print(a_set)
