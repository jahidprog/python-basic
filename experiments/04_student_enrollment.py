# Given a list of tuple with info(name, subject)
# 1. list all unique courses
# 2. list student enrolled in English
# 3. create dictionary (student and set of courses)

info = {
    ("Alice", "Math"),
    ("Bob", "English"),
    ("Charlie", "Math"),
    ("David", "English"),
    ("Charlie", "Science"),
    ("Frank", "Math"),
    ("Charlie", "English"),
    ("Heidi", "Science"),
    ("Ivan", "Math"),
    ("Judy", "English"),
    ("Kevin", "Science"),
}

# courses = set() #empty set
# for tup in info:
#     courses.add(tup[1])

# print(courses)

# for name, subject in info:
#     if subject == "English":
#         print(name)

dict = {}
for name, subject in info:
    if name not in dict:
        dict[name] = set()
    dict[name].add(subject)

print(dict)