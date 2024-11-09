from typing import Any, Dict

roll: int = 1

def add(base: Dict[int, Dict[str, Any]]) -> None:
    global roll
    name: str = input("Enter the name of the student: ")
    age: int = int(input("Enter the age of the student: "))
    number: int = int(input("Enter the total marks of the student: "))
    
    base[roll] = {'Name': name, 'Age': age, 'Marks': number}
    print(f"Student added with roll number: {roll}")
    roll += 1


def update(base: Dict[int, Dict[str, Any]]) -> None:
    roll_number: int = int(input("Enter the roll number of the student to update: "))
    if roll_number in base:
        name: str = input("Enter the new name of the student: ")
        age: int = int(input("Enter the new age of the student: "))
        number: int = int(input("Enter the new total marks of the student: "))
        base[roll_number] = {'Name': name, 'Age': age, 'Marks': number}
        print(f"Student record for roll number {roll_number} updated.")
    else:
        print("Student not found.")

def retrieve(base: Dict[int, Dict[str, Any]]) -> None:
    roll_number: int = int(input("Enter the roll number of the student to retrieve: "))
    if roll_number in base:
        print(f"Record for roll number {roll_number}: {base[roll_number]}")
    else:
        print("Student not found.")

def main() -> None:
    base: Dict[int, Dict[str, Any]] = {}
    
    while True:
        print("\nMenu:")
        print("1. Add Student")
        print("2. Update Student")
        print("3. Retrieve Student")
        print("4. Display All Students")
        print("5. Exit")
        
        choice: int = int(input("Enter your choice: "))
        
        if choice == 1:
            add(base)
        elif choice == 2:
            update(base)
        elif choice == 3:
            retrieve(base)
        elif choice == 4:
            print("All Student Records:")
            for roll_number, info in base.items():
                print(f"Roll Number: {roll_number}, Info: {info}")
        elif choice == 5:
            print("Exiting the system.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
