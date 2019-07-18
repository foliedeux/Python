from math import *

a = int(input("Enter side 1: "))
b = int(input("Enter side 2: "))
deg = int(input("Enter angle(in degrees): "))
c = sqrt(a**2 + b**2 - (2 * a * b * cos(radians(deg))))
print("The third side is ", c)