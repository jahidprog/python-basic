square = []
for i in range(6):
    square.append(i*i)
print(square)


# can do same using list comprehension
sq = [i*i for i in range(6)]
print(sq)

odsq = [i*i for i in range(6) if i%2 != 0] 
print(odsq)


arr = [-2, -4, -5, 3, 1, 5, -5, 1, 0]
arr = [0 if val < 0 else val for val in arr]
print(arr)

words = ["hello", "python", "jahid"]
words = [val.upper() for val in words]
print(words)