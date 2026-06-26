"""
Topic: Python Basics
Author: Kaushik Tambe
Purpose: Practice variables, data types, operators, type conversion, and user input.
"""

# -----------------------------
# Variable Assignment
# -----------------------------

name = "Kaushik"
age = 27
price = 5.5

# Getting data types
print(type(name))
print(type(age))
print(type(price))


# -----------------------------
# Different Ways to Define Strings
# -----------------------------

name1 = 'Kaushik'
name2 = "Kaushik"
name3 = '''Kaushik'''

print(name1)
print(name2)
print(name3)


# -----------------------------
# Boolean and None Values
# -----------------------------

age = 27
is_old = False
a = None

print(type(age))
print(type(is_old))
print(type(a))


# -----------------------------
# Assigning Variables
# -----------------------------

a = 100
b = 6

result = a - b

print(result)


# -----------------------------
# Arithmetic Operators
# -----------------------------

a = 5
b = 2

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)      # Remainder
print(a ** b)     # a raised to the power of b


# -----------------------------
# Relational Operators
# -----------------------------

a = 50
b = 20

print(a == b)     # False
print(a != b)     # True
print(a >= b)     # True
print(a > b)      # True
print(a < b)      # False
print(a <= b)     # False


# -----------------------------
# Assignment Operators
# -----------------------------

num = 10

num = num + 10
num += 10
num -= 10
num *= 10
num **= 10

print("Num:", num)


# -----------------------------
# Logical Operators
# -----------------------------

a = 50
b = 30

print(not True)
print(not (a > b))

val1 = True
val2 = False

print("AND Operator:", val1 and val2)
print("OR Operator:", val1 or val2)
print("OR Operator:", (a == b) or (a > b))


# -----------------------------
# Type Conversion
# -----------------------------

a = 2
b = 4.25

result = a + b

print(result)


# -----------------------------
# Type Casting
# -----------------------------

a = float("2")
b = 4.25

result = a + b

print(result)

a = 3.14
a = str(a)

print(type(a))


# -----------------------------
# User Input
# -----------------------------

value = int(input("Enter a number: "))
print(type(value), value)

name = input("Enter your name: ")
age = input("Enter your age: ")
marks = input("Enter your marks: ")

print("Welcome,", name)
print("Age:", age)
print("Marks:", marks)


# ======================================================
# Practice Questions
# ======================================================

# Question 1
# Input two numbers and print their sum.

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

result = num1 + num2

print(result)


# ------------------------------------------------------
# Question 2
# Input the side of a square and print its area.
# ------------------------------------------------------

side = float(input("Enter the length of the side: "))

area = side * side

print("The area of the square is:", area)


# ------------------------------------------------------
# Question 3
# Input two floating-point numbers and print their average.
# ------------------------------------------------------

x = float(input("Enter the first value: "))
y = float(input("Enter the second value: "))

average = (x + y) / 2

print("Average =", average)


# ------------------------------------------------------
# Question 4
# Input two numbers (a and b).
# Print True if a is greater than or equal to b.
# Otherwise, print False.
# ------------------------------------------------------

a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))

print(a >= b)
