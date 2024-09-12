s = "loveleetcode"
c = "e"

n = len(s)
answer = [0] * n

for i in range(n):
    min_distance = float('inf')  # Initialize to positive infinity for comparison

    for j in range(n):
        if s[j] == c:
            distance = abs(i - j)
            min_distance = min(min_distance, distance)

    answer[i] = min_distance

print(answer)
