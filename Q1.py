string = input("Enter your string: ")
count = 0
for ch in string:
    if ch in "aeiouAEIOU":
        count += 1
print(count)