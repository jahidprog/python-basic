# Dictionaries

student = {
    "name": "Jahid",
    "age": 25,
    "department": "CSE",
    "gpa": 3.22,
}

print(student["name"])

student["country"] = "Bangladesh"
student["gpa"] = 3.30

print(student)

for key, value in student.items():
    print(f"{key}: {value}")

print(student.get("email", "No email found"))
