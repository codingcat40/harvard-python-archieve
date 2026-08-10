def meow(n: int) -> str:
    return "meows \n" * n


number: int = int(input("Number : "))
meows: str = meow(number)
print(meows, end="")