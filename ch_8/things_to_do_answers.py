# 8.1
e2f = {"dog":"chien",
       "cat":"chat",
       "walrus":"morse"}
# 8.2
print(e2f["walrus"])

# 8.3
f2e = {}
for english, french in e2f.items():
    f2e[french] = english

# 8.4
print(f2e["chien"])

# 8.5
print(set(f2e.keys()))

# 8.6
life = {"animals":{"cats":["Henry","Grumpy","Lucy"],
                   "octopi":{},
                   "emus":{}},
        "plants":{},
        "other":{}}


# 8.7
print(life.keys())

# 8.8
print(life['animals'].keys())

# 8.9
print(life['animals']['cats'])

# 8.10
squares = {number:number * number for number in range(10)}
print(squares)

# 8.11
odd = {number for number in range(10) if number % 2 == 1}
print(odd)

# 8.12
for number in range(10):
    print("Got",number)

# 8.13 (Hint page 110)
tup1 = ('optimist','pessimist','troll')
tup2 = ('The glass is half full','The glass is half empty','How did you get a glass')
dict1 = dict(zip(tup1, tup2))
print(dict1)

# 8.14
titles = ['Creature of Habit','Crewel Fate','Sharks On a Plane']
plots = ['A nun turns into a monster.','A haunted yarn shop.','Check your exits.']
movies = dict(zip(titles,plots))
print(movies)
