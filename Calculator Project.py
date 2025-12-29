#The defining stage

operations = {
    "add": lambda a,b: a + b,
    "subtract": lambda a,b: a - b,
    "divide": lambda a, b: a / b if b != 0 else float('inf'),
    "multiply": lambda a,b: a * b,
    "exponent": lambda a,b: a ** b,
    "average": lambda a,b: (a + b)/2
}

a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))

q = input("What would you like to do with a and b in its respective order?").lower()

#Computational and output stage

if q in operations:
    r = operations[q](a,b)
else:
    r = ("Syntax error - try again!")

print(r)
