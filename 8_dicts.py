

# students = {
#     "Maddie": "Gry",
#     "Marrie": "Gry",
#     "Naman": "Sly",
#     "Maya": "Gry"
# }

# print(students["Naman"])

# for key in students:
#     print(key, students[key], sep=", ")


students = [

    {
        "name": "Hermione", "house": "Gryffindor", "patronus": "Otter"
    },
    {
        "name": "Harry", "house": "Gryffindor", "patronus": "Stag"
    },
    {
        "name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell terrier"
    },
    {
        "name": "Draco", "house": "Slytherin", "patronus": None
    }
]

for student in students:
    print(student["name"], student["house"], student["patronus"], sep=", ")
