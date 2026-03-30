nums = [23,42,12,35,23,23]

for n in nums:
    if nums.count(n) > 1:
        while nums.count(n) > 1:
            nums.remove(n)

print(nums)