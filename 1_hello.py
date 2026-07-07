# print('Hello Naman!')

name = input('Enter your full Name')
# age = int(input("what's your age?"))
# age += 1

# removing whitespace from str
name = name.strip()
# name = name.capitalize()

# name = name.title()
name = name.strip().title()

# split username into first and a last name

first, last = name.split(" ")


# """ 
# """
print(f"Hello {first}, I think you are a MAN") 
# print("Hello \n" + name)
# print("hello," ,name)

print("Hello,", end="")
print("Naman")

print("Hello, ", name, sep="!!!")

print("hello \"didi\"")