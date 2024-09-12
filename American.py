a = "qwertyuiop"
b = "asdfghjkl"
c = "zxcvbnm"
ans = []

words = ["Hello","Dad", "Peace"]

for i in words:
    y=i[0].lower()
    print(y)
    if y in a:
        x = a
    elif y in b:
        y = b
    else:
        y = c
    for j in i.lower():
        if j not in x:
            break
    else:
        ans.append(i)
    print(ans)
