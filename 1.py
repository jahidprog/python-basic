# WAP that takes salary as input. using conditional statement calculate the final tax rate based on these rule:
# if salary < 30000 --> 5% 
# if salary 30000 to 70000 --> 15%
# if salary > 70000 --> 20%

salary = int(input("Enter your salary: "))

tax = 0.0

if salary < 30000:
    tax = salary * 0.05
    print("Your salary is below 30k, your tax is:", tax)

elif salary < 70000:
    tax = salary * 0.15
    print("Your salary is between 30k and 70k, your tax is:", tax)

else:
    tax = salary * 0.20
    print("Your salary is above 70k, your tax is:", tax)
