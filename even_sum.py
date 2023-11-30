#Write a program that calculates and prints the sum of the even integers from 2 to 30.

sum = 0
for even_numbers in range(2,31,2):
    sum += even_numbers
print("Total sum of even number is: ", sum)