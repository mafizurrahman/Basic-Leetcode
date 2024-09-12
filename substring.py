s = "abcabcabcabc"
#
# new = []
# for i in range(len(s)):
#
#     if s[i] not in new:
#         new.append(s[i])
#
# merged_string = "".join(new)
# # count = 0
# count = s.count(merged_string)
#
# if count > 1:
#     print ("true")
# else:
#     print("false")
s_fold = "".join((s[1:], s[:-1]))

return (s in s_fold)