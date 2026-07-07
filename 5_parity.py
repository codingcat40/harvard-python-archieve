def main():
    x = int(input('what\'s x'))

    if isEven(x):
        print("Even")
    else:
        print("Odd")

    print(type(x))

def isEven(num):
    return True if num % 2 == 0 else False

main()