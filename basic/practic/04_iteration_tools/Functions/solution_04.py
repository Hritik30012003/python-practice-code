# Q Function returning Multiple values
#Create a function that returns both the area and circumference of a circle given its radius.

import math

def circle_stats(radius):
    area = math.pi * radius ** 2
    circumference = 2 * math.pi * radius ** 2
    return area, circumference

a, c = circle_stats(3)

print("Area:", a, "circumference:", c)
# homework- print only 2 digit after decimal
