#Write a Python function swap(i,j,l) 
# which interchanges the ith and jth elements in the list, l.
# Eg: Given a List with position of the element
# Input : List = [23, 65, 19, 90], pos1 = 1, pos2 = 3
# Output : [19, 65, 23, 90]

def swap(i,j,l):
    if 0 <= i < len(l) and 0 <= j < len(l):
        l[i], l[j] = l[j], l[i]
    else:
        print("Invalid position!")
        
list = [23, 65, 19, 90]
print("Before swapping", list)

pos1 = 1
pos2 = 3

swap(pos1, pos2, list)

print(f"After swapping: pos {pos1} and {pos2}", list)