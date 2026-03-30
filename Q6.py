list1 = [42, 21, 31, 4, 25]
list2 = [34, 25, 7, 4, 19]

common = []

for i, j in zip(list1, list2):
    if i == j:
        common.append( i )

print(common)