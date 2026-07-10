# with open("people.csv", "r") as file:
#     for line in file:
#         name, place = line.rstrip().split(",")
#         print(f"{name} is in {place}")

import csv

people = []

with open("people.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        
        people.append({"name": row["name"], "house": row["house"]})
    # for line in file:
    #     name, house = line.rstrip().split(",")
    #     person = {"name": name, "house": house}
    #     people.append(person)
# for person in sorted(people):
#     print(person)

# def get_name(person):
#     return person["name"]

# def get_house(person):
#     return person["house"]

# lambda anonymous function
for person in sorted(people, key=lambda person: person["name"]):
    print(f"{person["name"]} is in place {person["house"]}")
