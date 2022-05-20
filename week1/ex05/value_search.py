import sys
from os import EX_SOFTWARE


states = {
"Oregon" : "OR",
"Alabama" : "AL",
"New Jersey": "NJ",
"Colorado" : "CO"
}
capital_cities = {
"OR" : "Salem",
"AL" : "Montgomery",
"NJ" : "Trenton",
"CO" : "Denver"
}

if len(sys.argv) != 2:
    exit(EX_SOFTWARE)

capital = None
for item in capital_cities.items():
    if item[1] == sys.argv[1]:
        capital = item[0]
        break

if capital:
    for item in states.items():
        if item[1] == capital:
            print(item[0])
            break
else:
    print("Unkown capital city")