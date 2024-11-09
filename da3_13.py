student_groups:list[list[str]] = []
def add_group(student1, student2) -> None:
    student_groups.append([student1, student2])
def display_groups() -> None:
    print("Current student groups:")
    for i, group in enumerate(student_groups, start=1):
        print(f"Group {i}: {group}")
def modify_group(group_index, new_student1, new_student2) -> None:
    if 0 <= group_index < len(student_groups):
        student_groups[group_index] = (new_student1, new_student2)
    else:
        print("Invalid group index.")
while True:
    print("\nOptions: add, display, modify, exit")
    choice: str = input("Enter choice: ")
    if choice == "add":
        student1: str = input("Enter first student name: ")
        student2: str = input("Enter second student name: ")
        add_group(student1, student2)
    elif choice == "display":
        display_groups()
    elif choice == "modify":
        index: int = int(input("Enter group index to modify (1-based): ")) - 1
        new_student1: str = input("Enter new first student name: ")
        new_student2: str = input("Enter new second student name: ")
        modify_group(index, new_student1, new_student2)
    elif choice == "exit":
        break
    else:
        print("Invalid option. Try again.")
