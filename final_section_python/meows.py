# def meow(n: int) -> str:
#     """
    
#     Meow n times
    
#     :param n: Number of times to meow
#     :type n: int
#     :raise TypeError: If n is not an int
#     :return: A string of n meows one per line
#     :rtype: str
    
#     """
#     # above is doc string
    
#     return "meows \n" * n


# number: int = int(input("Number : "))
# meows: str = meow(number)
# print(meows, end="")




import sys

if len(sys.argv) == 1:
    print("meow")
elif len(sys.argv) == 3 and sys.argv[1] == "-n":
    n = int(sys.argv[2])
    for _ in range(n):
        print("meows")
    
else:
    print("usage: meows.py")