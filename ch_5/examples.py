# Create string variables
variable = 'Snap'
print(variable)
variable2 = "Crackle"
print(variable2)
var3 = 'Snap I have dubs " quotes'
print(var3)
var4 = "Snap I have sing ' quotes"
print(var4)
var5 = '''I am a multi line
string that goes on for a while, and you
don't know where I end.'''
print(var5)

# Empty strings
var_empty = ''
var_empty = ""
var_empty = """"""
var_empty = ''''''
print(var_empty)

# Make string with conversion
vara = str(98.6)
print(vara)
varb = str(1.0e4)
print(varb)
varc = str(True)
print(varc)

# Escape with \
palindrome = 'A man,\nA plan,\nA canal:,\nPanama.'
print(palindrome)
tabex = 'a\tbc'
print(tabex)
escape_quote = 'I need to escape a single \' mark'
print(escape_quote)
escape_quote = "I need to escape a dubs \" mark"
print(escape_quote)
literal_backslash = "C:\\temp\\myfile"
print(literal_backslash)
#Raw string negates backslash
raws = r"Type a \n to get a new line in a normal string."
print(raws)

# Combine strings by using +
vara = "My name is " + "Jared"
print(vara)
# Can also combine literal strings by having one after the other, not variables though
varb = "My name is " "Jared"
print(varb)
# Python doesn't add spaces for you when combining strings, but it does in the print statement
vara = "My"
varb = "Name"
varc = "Is"
vard = "Jared"
vare = vara + varb + varc + vard
print(vare)
print(vara, varb, varc, vard)


# Duplicate a string with * operator
vara = "4b" * 8
print(vara)

# Get a character in a string
letters = 'abcdefghijklmnopqrstuvwxyz'
print(letters[0])
print(letters[25])
# To start from the right side of the string use negative offsets
print(letters[-1])
print(letters[-26])


# Get a substring with a slice 0 is the beginning from the left, -1 is the beginning from the right
print(letters[:])
print(letters[20:])
print(letters[:20])
print(letters[12:15])
# Last three characters
print(letters[-3:])
# From 19 excluding xyz
print(letters[18:-3])
# From 6 characters from right excluding last 2 charcters
print(letters[-6:-2])
# From the start to the end every 7th character
print(letters[::7])
# From offset 4 to 19, every 3rd charactere
print(letters[4:20:3])
# Given a negative step size we can step backward through the string
print(letters[-1::-1])
# Or
print(letters[::-1])


# Get length with len()
varlen = len(letters)
print(varlen)
empty = ""
print(len(empty))


# Split values based on a separator
csvvalues = "Bill,Johnson,06/06/1944,Lake Tahoe,California,90210"
values = csvvalues.split(',')
print(values)
# If don't split on separator then split uses whitespace, newlines, spaces, tabs
thevals = "My dog ate my\thomework."
values = thevals.split()
print(values)


# Combine a list by using join
monster_list = ['Yeti', 'Bigfoot', 'Loch Ness Monster']
monster_joined_comma = ', '.join(monster_list)
print(monster_joined_comma)
monster_joined = '\n\n'.join(monster_list)
print(monster_joined)

# Substitute by using replace()
setup = "a duck goes into a bar"
replaced_str = setup.replace('duck','deer')
print(replaced_str)
replaced_str2 = setup.replace('a ','a famous ',100)
print(replaced_str2)
# Watch out
replaced_str3 = setup.replace('a','a famous',100)
print(replaced_str3)


# Remove leading or trailing whitespace ' ', '\t', '\n' with strip(), lstrip(), rstrip()
mystr = """   I like to watch Netflix.  I like
to watch The Office on Netflix.



"""
print(mystr.strip())
print(mystr.lstrip())
print(mystr.rstrip())
# Can also use strip to remove any leading or trailing characters in a multicharacter string
mystr2 = "What the....?!!!??!?!...."
print(mystr2.strip(".?!"))



# Search a string withh find() or index()
# If string not found find() returns -1 while index returns an error
poem = """Source LyricFind: Taproot

Overbearing panic attack entrenching my veins
In an hour I'll be OK I pray that this pain will go away permanently someday
I've seen more than I should have to I've seen this on my own
This song is a poem to myself it helps me to live
In case of fire break the glass and move on into your own, your own
Reoccurring drowning effect entrenching my brain
I hope you'll be OK someday so I can say that you moved on in the right way
We've seen this and we've breathed this and we've lived this on our own
This song is a poem to myself it helps me to live
In case of fire break the glass and move on into your own
This song is a poem to myself it helps me to live
In case of fire break the glass and move on into your own, your own
This song is a poem to myself it helps me to live
In case of fire break the glass and move on into your own
This song is a poem to myself it helps me to live
In case of fire break the glass and move on into your own, your own, your own, your own!
"""

print(poem.startswith("Source"))
print(poem.endswith("The End."))
# Find the offset of the word
print(poem.find("entrench"))
print(poem.index("entrench"))
# Search starting from the right
print(poem.rfind("entrench"))
print(poem.find("duck"))
# This would throw an exception since duck doesn't exist in the string
# print(poem.index("duck"))
# How many times does the word occur
print(poem.count("entrench"))



# Case
setup = 'a duck goes into a BAR...'
print(setup.capitalize()) # capitalize first word
print(setup.title()) #capitalize first letter of each word
print(setup.upper()) #all uppercase
print(setup.lower()) #all lowercase
print(setup.swapcase()) #swap upper and lower case
# Alignment
print(setup.center(30))
print(setup.ljust(30))
print(setup.rjust(30))



# Formatting strings, common replace variable operations
# Old style format_string % data
thetable = "DataPoints"
rowlimit = 100
# The %s inside the string means to interpolate a string.
# The number of % needs to match number of argss
thesql = """
select top %s *
from %s
""" % (rowlimit, thetable)
print(thesql)

# New style python 2.6 and up {} and format()
# Using {}
thetable = "Records"
rowlimit = 5
thesql = """
select top {} *
from {}
"""
thesql = thesql.format(rowlimit, thetable)
print(thesql)
# Using numbered arguments {}
theschema = "dbo"
thetable = "Audits"
rowlimit = 500
thesql = """
select top {1} *
from {2}.{0}
"""
thesql = thesql.format(thetable, rowlimit, theschema)
print(thesql)
# Using named arguments
thesql = """
select top {limit} *
from {schema}.{table}
"""
thesql = thesql.format(limit=10, schema='dbo', table='DataPages')
print(thesql)
# Alignment
string = "Hello my name is {:^10s}".format("Edgar Allen Poe")
print(string)
string = "Hello my name is {:^10s}".format("Bob")
print(string)


# Newest style: f-strings, type the letter f or F before the first quote
table = 'Datapoints'
limit = 10
sentence = f''''
select top {limit}
from {table}
'''
print(sentence)




