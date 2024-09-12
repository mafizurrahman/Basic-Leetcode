nums = [0,2,3,4,6,8,9]

start = None
output = []
for i in range(len(nums)):
    if start is None:
        start = nums[i]

    if i == len(nums) - 1 or nums[i + 1] != nums[i] + 1:
        end = nums[i]
        if start == end:
            output.append(f"{start}")
        else:
            # print(f"Range: {start} -> {end}")

            output.append(f"{start} -> {end}")
        start = None
print(output)

