#Python program to illustrate the intersection
# of two lists in most simple way
def intersection(Group1, Group2):
    Group3 = [value for value in Group1 if value in Group2]
    return Group3


# Driver Code
Group1 = [80, 50, 63, 20, 75]
Group2 = [66, 50, 20, 1]
print(intersection(Group1, Group2))
