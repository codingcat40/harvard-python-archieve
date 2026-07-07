
def main():
    name = input("whats your name? ")
    print(hello(name))
    print(hello())



def hello(name="Naman"):
    return f"Hello {name}"
    

main()

