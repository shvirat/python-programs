# This program finds the roots of a quadratic equation like "ax^2 + bx + c = 0"
import math
a = float(input("Enter value of a: "))
b = float(input("Enter value of b: "))
c = float(input("Enter value of c: "))
d = b**2 - (4*a*c)
if d < 0:
    print("Roots are complex and imaginary")
else:
    root1 = (-b + math.sqrt(d)) / (2*a)
    root2 = (-b - math.sqrt(d)) / (2*a)
    print("Roots are real and different")
    print("Root 1: ", root1)
    print("Root 2: ", root2)