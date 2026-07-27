class Wizard:
    def __init__(self, name):
        if not name:
            raise ValueError("Missing name")
        self.name = name
    ...




class Student(Wizard):
    def __init__(self, name, house):
        # reference to the Wizard class
        super().__init__(name)
        self.house = house
        
    ...


class Professor(Wizard):
    def __init__(self, name ,subject):
        super().__init__(name)
        self.subject = subject
        
    ...


wizard = Wizard("Albus")
student = Student("Harry", "Gryffindor")
professor = Professor("Severus", "Defense against the Dark Arts")
