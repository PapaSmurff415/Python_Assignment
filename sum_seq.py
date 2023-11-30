import sys

result = 0.0
a = len(sys.argv)

for i in range(1,a):
    result += float(sys.argv[i])
print("The sum sequence is: ", result)
