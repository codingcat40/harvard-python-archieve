
def first():
        n = int(input("Enter student score "))
        grade = ''

        if n >= 80:
            grade = 'A'
        elif n >= 70:
            grade = 'B'
        elif n >= 60:
            grade = 'C'
        elif n >= 50:
            grade = 'D'
        elif n >= 40:
            grade = 'E'
        else:
            grade = 'F'

        print(f"Student Grade is: {grade}")

def second():
        x = int(input('x value '))
        y = int(input('y value '))
        if x !=y:
            print("x is not equal to y")
        else:
            print('x equals y')
            
            
def main():
    second()


main()