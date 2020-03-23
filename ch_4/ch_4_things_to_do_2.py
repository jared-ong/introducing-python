small = input("Is the item small? (True/False):")
green = input("Is the item green? (True/False):")

if small == "True":
    small = True
else:
    small = False

if green == "True":
    green = True
else:
    green = False

if small:
    if green:
        print("This is a pea.")
    else:
        print("This is a cherry.")
else:
    if green:
        print("This is a watermelon.")
    else:
        print("This is a pumpkin.")
