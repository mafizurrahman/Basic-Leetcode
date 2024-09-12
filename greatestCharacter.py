letters = ['a', 'a', 'b']
sorted_letters = sorted(letters)
target = 'c'

add = []
for i in sorted_letters:
    if ord(target) < ord(i):
        # print(i)
        add.append(i)
    else:
        add.append(letters[0])
print(add[0])


# print(sorted_letters)

