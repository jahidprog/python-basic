# WAP take two intergers a and b and print even numbers between them:

a = int(input())
b = int(input())

for i in range(a, b+1):
    if i % 2 == 0:
        print(i)