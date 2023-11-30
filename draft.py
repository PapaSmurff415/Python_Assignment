#Write a Python function swap(i,j,l) 
# which interchanges the ith and jth elements in the list, l.
# Eg: Given a List with position of the element
# Input : List = [23, 65, 19, 90], pos1 = 1, pos2 = 3
# Output : [19, 65, 23, 90]
# [23, 90, 19, 65]

def swap(i,j,L):
    if 0 <= i < len(L) and 0 <= j < len(L):
        L[i], L[j] = L[j], L[i]
    else:
        print("invalid position!")


list = [23, 65, 19, 90]

pos1 = 1
pos2 = 3

swap(pos1, pos2, list)

print("After swapping", pos1, " and ", pos2, " we get ", list)