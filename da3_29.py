
course_1: set[str] = {"Alice", "Bob", "Charlie"}
course_2: set[str] = {"Charlie", "David", "Emma"}

all_enrolled: set[str] = course_1 | course_2
print("All enrolled:", all_enrolled)
both_courses: set[str] = course_1 & course_2
print("Both courses:", both_courses)
only_course_1: set[str] = course_1 - course_2
print("Only in Course 1:", only_course_1)
