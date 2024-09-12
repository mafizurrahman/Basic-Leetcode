arr = [1, 2, 2, 6, 6, 6, 6, 7, 10]

dict_count = {}
count = 0

for i in arr:
    if i in dict_count:
        dict_count[i] += 1
    else:
        dict_count[i] = 1

count_list = list(dict_count.values())
element_with_max_count = max(dict_count, key=dict_count.get)

max_count = max(count_list)

percentage = (max_count / len(arr)) * 100

if percentage >= 25:
    print(element_with_max_count)
