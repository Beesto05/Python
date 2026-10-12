python = {"ashik", "arun", "ajith"}
data_science = {"beesto", "ashik", "raghul"}
python.add("raju")
print(python)
data_science.remove("raghul")
print(data_science)
print(python & data_science)
print(python - data_science)
print(python | data_science)
students = {
    "python": 3,
    "data_science":3,
}

for course, count in students.items():
    print(f"Course: {course}, Students: {count}")

doubled_students = {course: count * 2 for course, count in students.items()}
print(doubled_students)