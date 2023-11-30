count = 0
even_num = 10

for i in range (1, even_num * 2 + 1):
    if i % 2 == 0:
        print(i)
        count += 1
    
    if count == 5:
        break