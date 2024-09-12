nums = [3,5]
count = 0

for x in range(len(nums)):
    if x <= nums[x]:
        count += 1


print(count)