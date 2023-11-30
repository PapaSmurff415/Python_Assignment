import sys

result = 0.0

s = len(sys.argv)

for i in range(1, s):
    result += float(sys.argv[i]) % s
print(result)