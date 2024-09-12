import itertools
my_list = [2,3,6,7]

all_combinations = []

# Iterate through all possible lengths of combinations
for r in range(1, len(my_list) + 1):
    # Generate combinations of length 'r'
    for combo in itertools.combinations(my_list, r):
        all_combinations.append(combo)

# Include an empty combination (an edge case)
all_combinations.append(())
n = 7
neew = []
# Print all combinations
for combo in all_combinations:
    if sum(combo) == n:
        neew.append(combo)
print(neew)

