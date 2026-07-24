import random


class Hat:
    # class variable, not an instance variable
    houses = ["Gry", "Huff", "Raven", "Slyth"]
    
    # class methods
    # classmethod decorator by default it is instancemethod
    @classmethod
    def sort(cls, name):
        print(name, "is in", random.choice(cls.houses))
    
Hat.sort("Harry")