#7.1
years_list = [1981,1982,1983,1984,1985]

#7.2
print(years_list[2])

#7.3
print(years_list[len(years_list) - 1])

#7.4
things = ["mozzarella","cinderella","salmonella"]

#7.5
things[1] = things[1].capitalize()
print(things)

#7.6
things[0] = things[0].upper()
print(things)

#7.7
things.remove("salmonella")
print(things)

#7.8 & 7.9
surprise = ["Groucho","Chico","Harpo"]
surprise[2] = surprise[2].lower()
surprise[2] = surprise[2][::-1].capitalize()
print(surprise)

#7.10
list2 = list(range(0,10,2))
print(list2)


#7.11
start1 = ["fee","fie","foe"]
rhymes = [("flop","get a mop"),
          ("fope","turn the rope"),
          ("fa","get your ma"),
          ("fudge","call the judge"),
          ("fat","pet the cat"),
          ("fog","walk the dog"),
          ("fun","say we're done")]
start2 = "Someone better"

for val in rhymes:
    line1 = " ".join([word.capitalize() + "!" for word in start1]) + " " + val[0].capitalize() + "!"
    line2 = start2 + " " + val[1] + "."
    print(line1)
    print(line2)
