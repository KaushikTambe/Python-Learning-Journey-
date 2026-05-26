# Multiplication Table Generator
# Learned: for loops, f-strings, user input
# Date: May 2026

table = int(input("Which table do you want? "))
for i in range(1, 11):
    print(f"{table} x {i} = {table * i}")
