#Write a program for printing the prime numbers which are less that number m, 
# which is supplied as command-line parameter.

import sys

def is_prime(num):
    if num < 2:
        return False
    
    for i in range (2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
        
    return True

if len(sys.argv) != 2:
    print("usage: python3 prime.py arg")
else:
        try:
            num = int(sys.argv[1])
            
            for num in range(2, num):
                if is_prime(num):
                    print(f"{num} is a prime number")
                else:
                    print(f"{num} is not a prime number")
        except ValueError:
            print("Enter a valid integer value")
