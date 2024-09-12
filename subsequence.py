s = "ab"
t = "baab"

n = ""
new = []
for j in t:
    if j in s:
            n += j


print(s,n)
if s == n or s in n:
    print("true")
else:
    print("false")

