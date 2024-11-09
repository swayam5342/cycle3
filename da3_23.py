from typing import Any, Dict
id: int = 1

def add(base: Dict[int, Dict[str, Any]]) -> None:
    global id
    name: str = input("Enter the name of the contact: ")
    phone_number: int = int(input("Enter the phone_number of the contact: "))
    email: str = str(input("Enter the total marks of the contact: "))
    base[id] = {'Name': name, 'phone_number': phone_number, 'mail': email}
    print(f"contact added with id number: {id}")
    id += 1


def update(base: Dict[int, Dict[str, Any]]) -> None:
    id_number: int = int(input("Enter the id number of the contact to update: "))
    if id_number in base:
        name: str = input("Enter the new name of the contact: ")
        phone_number: int = int(input("Enter the new phone_number of the contact: "))
        email: str = str(input("Enter the new email of the contact: "))
        base[id_number] = {'Name': name, 'phone_number': phone_number, 'mail': email}
        print(f"contact record for id number {id_number} updated.")
    else:
        print("contact not found.")

def retrieve(base: Dict[int, Dict[str, Any]]) -> None:
    id_number: int = int(input("Enter the id number of the contact to retrieve: "))
    if id_number in base:
        print(f"Record for id number {id_number}: {base[id_number]}")
    else:
        print("contact not found.")

def main() -> None:
    base: Dict[int, Dict[str, Any]] = {}
    while True:
        print("\nMenu:")
        print("1. Add contact")
        print("2. Update contact")
        print("3. Retrieve contact")
        print("4. Display All contacts")
        print("5. Exit")
        
        choice: int = int(input("Enter your choice: "))
        if choice == 1:
            add(base)
        elif choice == 2:
            update(base)
        elif choice == 3:
            retrieve(base)
        elif choice == 4:
            print("All contact Records:")
            for id_number, info in base.items():
                print(f"id Number: {id_number}, Info: {info}")
        elif choice == 5:
            print("Exiting the system.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
