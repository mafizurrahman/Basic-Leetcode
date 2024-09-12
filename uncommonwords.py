s1 = "this apple is sweet"
s2 = "this juice is sour"


s =  s1.split()+s2.split()
print(s)

dictionary = dict()

for i in s:
    if i not in dictionary:
        dictionary[i] = 1
    else:
        dictionary[i] +=1
new = []

for i in dictionary:
    if dictionary[i] == 1:
        new.append(i)
print(new)
