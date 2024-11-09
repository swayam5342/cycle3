from typing import Any, Dict
def add(base: Dict[str, Dict[str, Any]]) -> None:
    name: str = input("Enter the name of the student: ")
    registration_numbers: str = input("Enter the registration numbers of the student: ")
    marks:list[int]=[]
    for i in range(3):
        mark: int = int(input(f"Enter the marks of the student for subject {i+1}: "))
        marks.append(mark)
    base[name] = {'registration numbers': registration_numbers, 'Marks': marks}
    print(f"Student added with name : {name}")
def retrieve(base: Dict[str, Dict[str, Any]]) -> None:
    ma=0
    for i in base:
        ma:int=max(sum(base[i]['Marks']),ma)
    print(f"The maximum marks is : {ma}")
def main() -> None:
    base: Dict[str, Dict[str, Any]] = {}
    while True:
        print("\nMenu:")
        print("1. Add Student")
        print("2. Retrieve maximum marks")
        print("3. Exit")
        choice: int = int(input("Enter your choice: "))
        if choice == 1:
            add(base)
        elif choice == 2:
            retrieve(base)
        elif choice == 3:
            print("Exiting the system.")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()
