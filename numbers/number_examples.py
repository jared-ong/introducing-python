# BOOLEANS - True or False
x = bool(True)
print(x)
x = bool(1)
print(x)
x = bool(-45)
print(x)
x = bool(False)
print(x)
x = bool(0)
print(x)
x = bool(0.0)
print(x)


# INTEGERS (42 and 10000000)
x = 5
print(x)
x = 0
print(x)
# This will throw an error
05
x = 05

x = +123
print(x)
x = 123
print(x)
x = -123
print(x)

# This will throw an error
1,000,000
x = 1,000,000

# The underscore is a valid separator
x = 1_000_000
type(x)
print(x)
x = 0000
print(x)



# Integer Operations
# Addition
x = 5 + 8
print(x)
# Subtraction
x = 90 - 10
print(x)
# Multiplication
x = 4 * 7
print(x)
# Floating point division
x = 7/2
print(x)
# Integer truncating division
x = 7//2
print(x)
# Modulus
x = 7 % 3
print(x)
# Exponentiation
x = 3 ** 4
print(x)

# Addition and Subtraction
x = 5 + 9
print(x)
x = 100 - 7
print(x)
x = 4 - 10
print(x)
x = 5 + 9 + 3
print(x)
x = 4 + 3 - 2 - 1 + 6
print(x)
# Not required to have a space between each number
x = 5+9          +     3
print(x)

# Multiplication
x = 6 * 7
print(x)
x = 6 * 7 * 2 * 3
print(x)
# Division
x = 9 / 5
print(x)
x = 9 // 5
print(x)
# Divide by 0 throws error as expected
x = 5 / 0




# floats (numbers with decimal points 12.3333333 or 1.0e8)
x = 5.0
print(x)
x = 05.0
print(x)
x = 5.
print(x)
x = 5e0
print(x)
x = 5e1
print(x)



# Python precedence
x = 2 + 3 * 4
print(x)
x = 2 + (3 * 4)
print(x)
x = (2 + 3) * 4
print(x)


# Bases
# Integers are assumed to be base 10 unless you use a prefix to specify another
x = 10
print(x)
# Binary (Base 2 - uses 0 & 1)
# One (decimal) two and 0 ones
x = 0b10
print(x)
x = 0B10
print (x)
# Octal (Base 8 - uses 0 - 7)
# One (decimal) eight and 7 ones
x = 0o17
print(x)
# Hex (Base 16 - uses 0 - 9 and A - F )
# 4 (decimal) sixteen and 1 ones
x = 0x41
print(x)

# bin(), oct(), hex(), chr(), ord('A')
x = 65
y = bin(x)
print(y)
y = oct(x)
print(y)
y = hex(x)
print(y)
# chr function
x = chr(65)
print(x)
# ord goes the other way
x = ord('A')
print(x)


#Let's look at SQL jobs on a SQL server jobID is actually a Hex value look in ApplicationName column of dbamon.dbo.trace
# select * from dbamon.dbo.trace
# select * from msdb.dbo.sysjobs where job_id = 0x0EBD4F3BC1C8A64D82D698F7E6AA9E67
# select CAST(0x0EBD4F3BC1C8A64D82D698F7E6AA9E67 AS UNIQUEIDENTIFIER) AS Job_Unique_ID
x = 0x0EBD4F3BC1C8A64D82D698F7E6AA9E67
print(x)


# Type conversions
# int() - in Python 2 int was -2,147,483,648 to 2,147,483,648 but in Python 3 an int can be any size including a googol (one followed by 100 zeroes, named in 1920 by a 9 year old boy.
# Googolplex - 1 plus a thousand zeroes originally suggested as the name for Google, but they settled on googol but didn't check it's spelling before registering google.com domain
x = int(True)
print(x)
x = int(False)
print(x)
x = int('99')
print(x)


# bool()
x = bool(1)
print(x)
x = bool(0)
print(x)
x = bool(55)
print(x)


# float
x = float(True)
print(x)
x = float(False)
print(x)
x = float(98)
print(x)
x = float('1.0e4')
print(x)

# Python also promotes booleans to integers to floats
x = False + 0
print(x)
x = False + 0.0
print(x)
x = True + 1
print(x)
