def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print("Number\tFactorial")

for i in range(1, 6):
    result = factorial(i)
    
    print(f"{i}\t{result}")
