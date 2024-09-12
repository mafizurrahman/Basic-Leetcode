s = "abcd"
t = "abcdd"

s = sorted(s)
t = sorted(t)
i = 0
j = 0
new = []
while i < len(s) and j < len(t):
    if s[i] != t[j]:
        print(t[j])
    else:
        i += 1
        j += 1
print(t[-1])
