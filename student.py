def main():
    student = get_student()
    if student["house"] == "Auroville":
        student["name"] = "Annie"

    print(f"{student['name']} from {student["house"]}")


def get_student():
    # student = dict()
    # student["name"] = input("Name: ")
    # student["house"] = input("House: ")
    name = input("Name: ")
    house = input("house: ")
    
    return {"name": name, "house": house}


if __name__ == "__main__":
    main()