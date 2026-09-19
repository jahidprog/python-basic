# File Handling

file_name = "example.txt"

# Write
with open(file_name, "w", encoding="utf-8") as file:
    file.write("Python is fun!\n")
    file.write("I'm learning Python for GenAI.\n")

# Read
with open(file_name, "r", encoding="utf-8") as file:
    content = file.read()

print(content)

# Append
with open(file_name, "a", encoding="utf-8") as file:
    file.write("Keep building.\n")
