s = "aabb"

dict_list = dict()
for i in range(len(s)):
    if s[i] not in dict_list:
        dict_list[s[i]] = 1
    else:
        dict_list[s[i]] += 1
print(dict_list)

for i in dict_list:
    if dict_list[i] == 1:
        k = i
        break

# print(k)
result  = []
for a in range(len(s)):
    if s[a] == k:
        result.append(a)
        break
print(result)

if len(result) == 1:
    print(result[0])
else:
    print("-1")




