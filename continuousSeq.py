nums = [1, 3, 5, 2, 1]

current = []
largest = []
count = 0
for i in range(len(nums) - 1):
    if nums[i] < nums[i + 1]:
        current.append(nums[i])
    else:
        current.append(nums[i])
        if len(current) > len(largest):
            largest = current

    current = []

current.append(nums[-1])

if len(current) > len(largest):
    largest = current

print(len(largest))
