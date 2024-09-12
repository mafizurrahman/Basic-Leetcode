nums = [1, 2, 3, 6]

j = max(nums)
print("Maximum value:", j)

for i in range(len(nums)):
    if j > (nums[i] * 2):
        print(j, "is greater than 2x", nums[i])
    if nums[i] == j:
        print("Location of the maximum value:", i)
    else:
        print(nums[i], "is smaller than the maximum value.")
