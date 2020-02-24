#Variables
varbool = True
varint = 6
varfloat = 3.23232
varstring = "what to do with this string"
varstring2 = '''what to do
with
this string'''
varstring3 = 'what to do with this string'
varlist = [1,2,3,4,5]
vartuple = (1,2,3,4,5)
vardictionary = {'item1': 'ping pong', 'item2': 'basketball', 'item3': 'football'}

type(varbool)
type(varint)
type(varfloat)
type(varstring)
type(varstring2)
type(varstring3)
type(varlist)
type(vartuple)
type(vardictionary)

# Lists are mutable while tuples are not
varlist[2] = 5
varlist
# This will generate an error as tuples are immutable
vartuple[2] = 5


#Assignment of variables
y = 5
x = 12 - y
x

# list the python id of x and y
id(x)
id(y)

# list the type of variable
type(x)
type(y)

# Get reference count of a variable in python will return lots of ref counts due to compiled code referencing small integers a lot
# https://stackoverflow.com/questions/45013663/understanding-sys-getrefcount-differences-in-result
import sys
print(sys.getrefcount(x))
print(sys.getrefcount(y))

# Show a large number refcount
bill = 12415151515
print(sys.getrefcount(bill))
jared = bill
print(sys.getrefcount(bill))
print(sys.getrefcount(jared))
jared = 1234
print(sys.getrefcount(bill))
print(sys.getrefcount(jared))
