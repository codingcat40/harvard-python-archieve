# appending

# name = input("what's your name")


# with open("names.txt", "a") as file:
#     file.write(f"{name}\n")


# reading
names = []

with open("names.txt", "r") as file:
    for line in file:
        # print("hello", line.rstrip())
        names.append(line.rstrip())

for name in sorted(names, reverse=False):
    print(f"hello, {name}")
