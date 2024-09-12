nums = [1, 12, -5, -6, 50, 3]
k = 4
curr_max = float("-inf")  #negative numbers

for i in range(len(nums) - k + 1):
    subarray_sum = sum(nums[i:i+k])
    # print(nums[i:i+k])
    curr_max = max(curr_max, subarray_sum)

print(curr_max) 