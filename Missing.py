nums = [9,6,4,2,3,5,7,0,1]
l1 = []
# c= []
for i in range(0, len(nums)+1):
    if i not in nums:
        l1.append(i)

print(l1)