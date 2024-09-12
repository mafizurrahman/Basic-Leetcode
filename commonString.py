nums = [1, 2, 3, 4]
new = []

for i in range(len(nums)):
    for j in range(len(nums)):
        if nums[i] != nums[j]:
            if [nums[j],nums[i]] not in new:
                new.append([nums[i], nums[j]])


min_sums = [min(pair) for pair in new]

# Find the maximum of the minimum sums
max_min_sum = max(min_sums)
print(max_min_sum)
