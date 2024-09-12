arr = [400]
new = []

for i in range(len(arr)):
    if i == len(arr) - 1:
        new.append(-1)
    else:
        max_num = max(arr[i+1:])
        new.append(max_num)


print(new)
