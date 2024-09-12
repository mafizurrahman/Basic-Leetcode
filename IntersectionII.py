nums1 = [1, 2, 1, 2]
nums2 = [2, 2]

nums1.sort()
nums2.sort()
c =[]
i = j = 0

while i < len(nums1) and j < len(nums2):

    if nums1[i] < nums2[j]:
        i += 1
    elif nums1[i] < nums2[j]:

        j +=1
    else:
        c.append(nums1[i])
        i += 1
        j += 1
print(c)