nums = [2, 1, 1, 1, 1, 1]
n = nums + [0]
count = 0
for i in range(0, len(n) - 1):
    if n[i] == 1 and n[i+1] == 1:
        count += 1
print(count)
