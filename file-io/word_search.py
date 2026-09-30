data = True
line = 1
word = "jahid"
with open("file-io/data.txt","r") as f:
    while data:
        data = f.readline()
        if word in data:
            print(f"{word} found in line : {line}")
        line += 1
