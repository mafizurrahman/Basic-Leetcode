nums = [1,1,1,1,1]
sum = []
sum.append(nums[0])
d = nums[0]
# k = nums [0]
for i in range(1, len(nums)):
    d = nums[i] + d
    sum.append(d)
print(sum)