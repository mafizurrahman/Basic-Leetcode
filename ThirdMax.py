nums = [2,2,3,1]



d = max(nums)
new = []
final = []

for i in range(len(nums)):
    # print(nums[i])
    if (nums[i] < d):
        new.append(nums[i])

# print(new)
sec = max(new)

for j in range(len(new)):
    if(new[j] < sec):
        final.append(new[j])

print(final)

print(max(final))




# for i in range(len(nums)):
#     p = max()