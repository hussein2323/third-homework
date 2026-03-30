st = input("Enter your string: ")
count = 0
for ch in st.lower():
    if ch in "aeiou":
        count += 1
print(count)