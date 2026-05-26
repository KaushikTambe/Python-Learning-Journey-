# Multiplication Table Generator
# Learned: for loops, f-strings, user input
# Date: May 2026

Table = int(input("Which table do you want? "))
for i in range(1,11):
    print(f"{Table} x {i} = {Table * i}")
