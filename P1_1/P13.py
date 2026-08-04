# Progam to display max of 3 numbers

a = int(input("Enter First Number  "))
b = int(input("Enter Second Number  "))
c = int(input("Enter Third Number  "))
m = a
if m < b:
    m = b
if m < c:
    m = c

print("Max Value is  ", m)