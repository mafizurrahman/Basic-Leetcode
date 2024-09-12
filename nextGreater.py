nums1 = [4, 1, 2]
nums2 = [1, 3, 4, 2]
c = []
for i in range(len(nums1)):
    for j in range(len(nums2)):

        if nums1[i] == nums2[j]:

            if nums2[j] < nums2[j+1]:

                c.append(nums2[j+1])
            else:
                c.append(-1)
print(c)
