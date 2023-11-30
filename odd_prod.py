#Write a program that calculates and prints the product of odd integers from 1 to 15.
odd_prod = 1
print("The product of odd number from 1 to 15:")
for odd_num in range(1, 16, 2):
    odd_prod = odd_num * odd_prod
    print(odd_prod)
