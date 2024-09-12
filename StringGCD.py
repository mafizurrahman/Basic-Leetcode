s1 = "ABABAB"
s2 = "ABAB"
s3 = ""

i = 0  # Initialize i and j
j = 0

while i < len(s1) and j < len(s2):
    if s1[i] != s2[j]:
        print("null")
        break

    if s1[i] == s2[j]:
        s3 += s1[i]
        i += 1
        j += 1
    else:
        i += 1

# print(s3)
s4 = ""
for i in range(len(s1)):
    s4 += s3
    # print(i, " ", s4)
    if s4 == s1:
        break
print(s3)

