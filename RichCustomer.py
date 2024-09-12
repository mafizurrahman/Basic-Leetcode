account = [[1,5],[7,3],[3,5]]
d = 0
sum = []
for i in account:
    for j in i:
        # print(j, end=' ')
        d = j + d
    # print(d)
    sum.append(d)
    d = 0
print(max(sum))