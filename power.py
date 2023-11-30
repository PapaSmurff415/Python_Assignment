#Write a recursive function power (base, exponent) that when invoked returns
#base exponent
#E.g., power (3,4) = 3x3x3x3. Assume that exponent is an integer greater than or equal
#to 1. Hint: The recursion step would use the following relationship
#base exponent = base x base exponent-1
#and the terminating condition occurs when exponent is equal to 1 because
#base 1 = base

def power(base, exponent):
    if exponent == 1:
        return base
    else:
        return base * power(base, exponent - 1)

base = int(input("Enter the base value:"))
exponent = int(input("Enter the exponent value:"))

result = power(base, exponent)
print(result)