interval = [1,4]

duration = 2
c = []
for i in range(len(interval)):
    c.append(interval[i])
    calc = interval[i] + duration - 1
    c.append(calc)

if len(c) != len(set(c)):
    print(len(set(c)))

else:
    print(len(c))
# print(c)