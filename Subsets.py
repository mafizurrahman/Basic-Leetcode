def sublists(lst):
    n = len(lst)
    sublists = [[0]]

    for i in range(n):
        for j in range(i + 1, n + 1):
            sublists.append(lst[i:j])

    return sublists


original_list = [1, 2, 3]
sublists_nested = sublists(original_list)
print(sublists_nested)
