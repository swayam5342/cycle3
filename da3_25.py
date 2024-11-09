
student_grades: dict[str, int] = {"Alice": 85, "Bob": 92, "Charlie": 78, "David": 88}
sorted_grades = dict(sorted(student_grades.items(), key=lambda x: x[1]))
print("Sorted student grades by values:", sorted_grades)


