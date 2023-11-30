#Write a program that evaluates the factorials of the integers from 1 to 5. 
# Print the results in tabular format. 

print("Number\tFactorial")
print("-----------------")
num = 1
for i in range(1, 5):
        num = num * i
        print(f"{i}\t{num}")
