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
            
            print(f"showing all the prime numbers from 2 to less than user supplied nth {num}:")
            
            for num in range(2, num):
                if is_prime(num):
                    print(num)
                    
        except ValueError:
            print("Enter a valid positive integer value")
