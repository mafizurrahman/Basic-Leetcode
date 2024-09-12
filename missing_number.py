nums = [1,7,3,6,5,6]

right = []
left = []
for i in range(len(nums)):

    leftcount = sum(nums[:i])
    # print(leftcount)
    left.append(leftcount)

    rightcount = sum(nums[i+1:])
    right.append(rightcount)

for i in range(len(left)):
    if left[i] == right[i]:
        print(i)
    else:
        print("not matched")