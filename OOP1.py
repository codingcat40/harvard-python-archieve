class Student:
    # methods
    # initialize an object
    def __init__(self, name, house, patronous):
        if not name:
            raise ValueError("Missing name")
        if house not in ["Auroville", "Chennai", "Pondicherry", "Bangalore", "Kochi"]:
            raise ValueError("Invalid house")
        self.name = name
        self.house = house
        self.patronous = patronous
        
    def __str__(self):
        return f"{self.name} from {self.house}"
        
    def charm(self):
        match self.patronous:
            case "Stag": 
                return "staggie"
            case "Otter":
                return "otterie"
            case _:
                return "Naah No patronous"
        

def main():
    student = get_student()

    # print(f"{student.name} from {student.house}")
    print("Expecto Patronum!")
    print(student.charm())

def get_student():
    # object as a instance of a class
    # student = Student()
    
    # student.name = input("Name: ")
    # student.house = input("House: ")
    
    
    name = input("Name: ")
    house = input("House: ")
    patronous = input("Patronous: ")
        
    # constructor
    return Student(name, house, patronous)


if __name__ == "__main__":
    main()