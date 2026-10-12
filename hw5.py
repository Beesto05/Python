
frontend = {"Arun", "Priya", "Kavin", "Divya"}
backend = {"Priya", "Kavin", "Rahul", "Meena"}

backend.add("Vijay")

frontend.remove("Divya")

both_courses = frontend & backend
print("Students in both courses:", both_courses)

backend_only = backend - frontend
print("Students only in Backend:", backend_only)

all_students = frontend | backend
print("Total unique students:", len(all_students))

course_counts = {
    "Frontend": len(frontend),
    "Backend": len(backend)
}

for course, count in course_counts.items():
    print(f"Course: {course}, Students: {count}")

fullstack_counts = {
    course: count for course, count in course_counts.items()
}
fullstack_counts["Fullstack"] = sum(course_counts.values())

print("Updated course dictionary:", fullstack_counts)
