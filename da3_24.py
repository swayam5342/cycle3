from typing import Any, Dict

def add(base: Dict[str,int]) -> None:
    global roll
    name: str = input("Enter the name of the student: ")
    marks=int(input("Enter the marks of the Student"))
    base[name]=marks
    print(f"student added with name : {name} , Marks : {marks}")
    

def retrieve(base: Dict[str,int]) -> None:
    ma=85
    for i,j in base.items():
        if j >=ma:
            print()
            print(f'{i} : {j}')


def main() -> None:
    base: Dict[str,int] = {}
    while True:
        print("\nMenu:")
        print("1. Add Student")
        print("2. Retrieve Student")
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
