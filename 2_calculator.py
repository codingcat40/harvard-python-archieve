# x = float(input('what is x? '))
# y = float(input('what is y? '))

# # z = round(x + y)

# # print(f"{z:,}")

# z = (x / y)

# print(f"{z:.6f}")


def main():
    x = int(input('value x'))
    print("X squared is", square(x))

def square(x):
    return x**2
    

main()