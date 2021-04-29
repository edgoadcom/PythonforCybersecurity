#!/usr/bin/env python3
# Script that tells us how many people there are in space
#By Ed Goad
# date: 2/5/2021

# Import Python modules
import requests
import json

def get_people_in_space():
    request_uri = "http://api.open-notify.org/astros.json"   
    r = requests.get(request_uri)
    items = r.json()
    return items

astronauts = get_people_in_space()

# print basic details
print(astronauts)

# print "pretty" json
print(json.dumps(astronauts, indent=2))

# search through data to return specific information
print("There are {0} people in space right now".format( \
    astronauts["number"]))
print("The first astronaut is {0} aboard the {1}".format( \
    astronauts["people"][0]["name"], \
    astronauts["people"][0]["craft"]))

# Loop through all the people
print("Full list of peole in space")
for person in astronauts["people"]:
    print("{0} is aboard the {1}".format(person["name"], \
    person["craft"]))