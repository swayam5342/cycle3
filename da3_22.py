from typing import Any, Dict
def add(base: Dict[int, Dict[str, Any]]) -> None:
    global roll
    name: str = input("Enter the name of the Book: ")
    isbn: int = int(input("Enter the ISBN number of the book: "))
    year: int = int(input("Enter the year of publiction : "))
    base[isbn] = {'Name': name, 'year':year}
    print(f"Book added with name : {name} , ISBN : {isbn}")
def retrieve(base: Dict[int, Dict[str, Any]]) -> None:
    isbn: int = int(input("Enter the ISBN to retrieve the info: "))
    if isbn in base:
        print(f"Record for ISBN number {isbn}: {base[isbn]}")
    else:
        print("ISBN number not found in the database.")
def main() -> None:
    base: Dict[int, Dict[str, Any]] = {}
    while True:
        print("\nMenu:")
        print("1. Add BOOK")
        print("2. Retrieve BOOK")
        print("3. Display All BOOK")
        print("4. Exit")
        
        choice: int = int(input("Enter your choice: "))
        
        if choice == 1:
            add(base)
        elif choice == 2:
            retrieve(base)
        elif choice == 3:
            print("All BOOK Records:")
            for isbn, info in base.items():
                print(f"ISBN: {isbn}, Info: {info}")
        elif choice == 4:
            print("Exiting the system.")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()
