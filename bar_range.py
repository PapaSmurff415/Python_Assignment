import matplotlib.pyplot as plt

bar = "*"
num_str = input("Enter any number:")
num_str = int(num_str)

for i in range(1, num_str):
    print(i * bar)

plt.bar(range(1, num_str), range(1, num_str))
plt.xlabel('Input Number')
plt.ylabel('Value')
plt.title('Bar Chart')
plt.show()
