f = open("file-io/data.txt", "r") #file object

# data = f.read()
data = f.readline()
print(data)
f.close()