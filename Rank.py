score = [11,4,1, 3,2]

sorted_scores = sorted(score, reverse=True)
rank_dict = {}
# print(rank_dict)
# Loop through the sorted scores and assign ranks
for i, s in enumerate(sorted_scores):
    if i == 0:
        rank_dict[s] = "Gold Medal"
    elif i == 1:
        rank_dict[s] = "Silver Medal"
    elif i == 2:
        rank_dict[s] = "Bronze Medal"
    else:
        rank_dict[s] = str(i + 1)

# Create a list to store the results
result = []

print(rank_dict)
# Loop through the input array and append the rank of each score to the result list
for s in score:
    # print(s)
    result.append(rank_dict[s])

# Return the result list
print(result)








