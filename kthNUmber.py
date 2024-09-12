n = 4
k = 4
new = []

for i in range(1, n + 1):
    if n % i == 0:
        new.append(i)

print(sorted(new))
if k > len(new):
   print("-1")
else:
    print(new[k-1])