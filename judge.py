nums = [[1, 3], [2, 3]]
n = 3
new = []
new1 = []

for sublist in nums:
    if sublist[0] <= n and sublist[1] <= n:
        new.append(sublist[0])
        new1.append(sublist[1])

if len(new) == len(set(new)) and len(new1) == 1 and new1[0] not in new:
    print("unique and same")
else:
    print("-1")
