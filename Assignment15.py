#Q15 Program to find the value of x^(y+z)

import math
x=int(input("Enter the value of x"))
y=int(input("Enter the value of y"))
z=int(input("Enter the value of z"))
a=y+z
b=pow(x,a)
print("The value is",b)