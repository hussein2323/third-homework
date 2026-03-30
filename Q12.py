def largest_number(numbers):
    if numbers:
        largest = max(numbers)
        print("The largest number is:", largest)
    else:
        print("list is empty.")


n = int(input("enter the length of the list: "))
num_list = []
for i in range(n):
    num = int(input("enter the number: "))
    num_list.append(num)

largest_number(num_list)