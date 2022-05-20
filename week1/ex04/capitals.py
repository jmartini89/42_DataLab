from os import EX_OK, EX_SOFTWARE
import sys


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

ret = capital_cities.get(states.get(sys.argv[1]))
if not ret:
    print("Unknown state")
else:
    print(ret)