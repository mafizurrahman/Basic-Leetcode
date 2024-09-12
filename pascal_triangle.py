from itertools import combinations

arr = [3, 1, 2, 4]
new = []

# Generate combinations of different lengths
for r in range(1, len(arr) + 1):
    for combo in combinations(arr, r):
        new.append(list(combo))

print(new)
res = []
# Calculate the sum for each combination
for i in range(len(new)):
    p = min(new[i])
    # print(f"Sum of {new[i]}: {p}")
    res.append(p)
print(sum(res))
