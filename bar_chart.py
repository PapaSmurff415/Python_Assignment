#One interesting application of computers is drawing graphs and bar charts. 
# Write a program that reads five numbers (each between 1 and 30) and 
# print a bar chart. 
# E.g., if your program reads the number 7, it should print *******.

import matplotlib.pyplot as plt

numbers = []

for i in range(1,6):
    while True:
        num_str = input(f"{i} Enter a number between 1 to 30: ")
        num = int(num_str)

        if 1 <= num <= 30:
            numbers.append(num)
            break
        else:
            print("Enter number between 1 to 30")
        
for num in numbers:
    print(num * '*')

plt.bar(range(1,6), numbers)
plt.xlabel('input number')
plt.ylabel('value')
plt.title('Bar graph')
plt.show()