numbers = [31, 6, 17, 12, 4, 31, 25]

Not_duplicated = []

for num in numbers:
    if num not in Not_duplicated:
        Not_duplicated.append(num)

print(" before :", numbers)
print(" after  removing:", Not_duplicated)