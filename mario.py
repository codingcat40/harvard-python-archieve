
def main():
    print_square(4)
    height = take_input()
    print_column(height)
    
def print_column(height: int):
    for i in range(height):
        print("#"*(i + 1))

def take_input():
    n = int(input("Enter a height"))
    return n


def print_square(size: int):
    for i in range(size):
        print("#"*size)

        print()

main()