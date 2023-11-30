#1.	Define a function called hypotenuse that calculates the length of the hypotenuse 
# of a right triangle when the two sides are given. 
# Use this function in a program to determine the 
# length of the hypotenuse of a triangle. 
# The function should take two arguments and return the hypotenuse. 

import math

def hypotenuse(h_side1, h_side2):
    #result = float (math.sqrt(h_side1**2 + h_side2**2))
    result = h_side1**2 + h_side2**2
    return result
    
s1 = float(input("Enter value1: "))
s2 = float(input("Enter value2: "))

print(hypotenuse(s1, s2))
