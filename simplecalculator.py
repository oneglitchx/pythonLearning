# Taking user input for first number 
int1 = int(input("Enter first number: "))
# Taking user input for the operator 
operator = input("Enter operator (+, -, *, /, **, %, //): ")
# Taking user input for second number
int2 = int(input("Enter second number: "))

# The main logic of the calculator 

if operator == "+":
    print(f"The sum of {int1} and {int2} is {int1 + int2}".title())
elif operator == "-":
    print(f"The difference of {int1} and {int2} is {int1 - int2}".title())
elif operator == "/":
    if int2 != 0:
        print(f"The division of {int1} by {int2} is {int1 / int2}".title())
    else:
        print("Division by zero is not allowed. Please enter a valid second number.")
elif operator == "*":
    print(f"The product of {int1} and {int2} is {int1 * int2}".title())
elif operator == "**":
    print(f"{int1} raise to the power {int2} is {int1 ** int2}".title())
elif operator == "//":
    if int2 != 0:
        print(f"The division of {int1} by {int2} and the quotient without decimal is {int1 // int2}")
    else:
        print("Division by zero is not allowed. Please enter a valid second number.")
elif operator == "%":
    if int2 != 0:
        print(f"The sum remainder of {int1} divided by {int2} is {int1 % int2}".title())
    else:
        print("Division by zero is not allowed. Please enter a valid second number.")
else:
    print("Invalid operator entered.")

