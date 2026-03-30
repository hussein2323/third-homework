nums = []

n = int(input("enter the length of the list: "))


for i in range(n):
    num = int(input("enter the number: "))
    nums.append(num)

largest = nums[0]

for x in nums:
    if x > largest:
        largest = x

print("the largest number is : ", largest )