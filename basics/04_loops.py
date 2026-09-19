# Loops

print("For loop:")
for i in range(1, 6):
    print(i)

print("\nWhile loop:")
count = 1
while count <= 5:
    print(count)
    count += 1

print("\nBreak:")
for i in range(10):
    if i == 5:
        break
    print(i)

print("\nContinue:")
for i in range(6):
    if i == 3:
        continue
    print(i)
