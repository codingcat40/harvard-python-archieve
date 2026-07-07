def get_init():
    while True:
        try:
            x =  int(input('What\'s x?'))
            return x
            # print(f"x is {x}")
        except ValueError:
            # print("x is not an integer")
            pass
        
    
def main():
    x = get_init()
    print(f"x is {x}")
# types of errors
# 1. ValueError

main()