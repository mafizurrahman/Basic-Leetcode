son = [1,2]
cookies = [1,2,3]
sum = 0
for i in cookies:
    sum = sum + i
# print(sum)
count = 0
add = 0

for i in son:
    # print("i value ", i)
    if i <= sum:
        count += 1
        sum = sum - i
        # print(add)
        if add < 0:
            break

print(count)

