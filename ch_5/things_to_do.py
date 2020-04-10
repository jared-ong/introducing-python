#5.1
song = """When an eel grabs your arm,
And it causes great harm,
That's - a moray!"""
song = song.replace(" m"," M")
print(song)

#5.2
questions = ["We don't serve strings around here. Are you a string?",
             "What is said on Father's Day in the forest?",
             "What mmakes the sound 'Sis! Boom! Bah!'?"]
answers = ["An exploding sheep.",
           "No, I'm a frayed knot.",
           "Pop! goes the weasel."]

print ("Q:" + questions[0] + '\n' + "A:" + answers[1])
print ("Q:" + questions[1] + '\n' + "A:" + answers[2])
print ("Q:" + questions[2] + '\n' + "A:" + answers[0])

#5.3
string = """
My kitty cat likes %s,
My kitty cat likes %s,
My kitty cat fell on his %s
And now thinks he's a %s
"""
print(string % ('roast beef', 'ham', 'head', 'clam'))

#5.4 and 5.5
letter = """
Dear {salutation} {name},

Thank you for your letter. We are sorry that our {product}
{verbed} in your {room}.  Please note that it should never be used in a {room},
especially near any {animals}.

Sincerely,
{spokesman}
"""
print(letter.format(salutation="Mr.", name="Bob", product="cheeseburger", verbed="barfed", room="bedroom", animals="dogs", spokesman="Jared"))

#5.6
names = ["boat", "horse", "train"]
for name in names:
    name = name.capitalize()
    print("%sy Mc%sface" % (name, name))

#5.7
for name in names:
    name = name.capitalize()
    print("{0}y Mc{0}face".format(name))

#5.8
for name in names:
    name = name.capitalize()
    string = f"{name}y Mc{name}face"
    print(string)
