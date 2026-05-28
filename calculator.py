# Simple Calculator
# Learned: if/elif/else, float input, operators
# Date: 28-05-2026

First_number = float(input("What is your first number? "))
Operator = input("use operator (+,-,*,/) ")
Second_number = float(input("What is your Second number? "))

# Operator used in the terminal
if Operator == "+":
    print(First_number + Second_number)
elif Operator == "-":
    print(First_number - Second_number)
elif Operator == "*":
    print(First_number * Second_number)
elif Operator == "/":
    # Cant divide by zero error
    if First_number == 0 or Second_number == 0:
        print("You can't divide a number with 0")
    else:
        print(First_number / Second_number)
# If user enters wrong operator
else:
    print("Error")
