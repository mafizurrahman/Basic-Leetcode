nums = [1,2,3,1]
k = 3

hset = {}

for i in range(len(nums)):

    if nums[i] in hset and abs(i - nums[i]) <=k:
        print("1")

    hset[nums[i]] = 1

print("@")

