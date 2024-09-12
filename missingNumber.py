nums = [1,1]
l = len(nums)
# print(l)
same = []
new = []
for i in range(len(nums)):
    c = i+1
    print(c)

    if c == nums[i]:
        same.append(nums[i])
    else:
        new.append(nums[i])
        new.append(c)
        # same.append(c)
print(new)




