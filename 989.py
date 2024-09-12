# Input: num = [1,2,0,0], k = 34
# Output: [1,2,3,4]
# Explanation: 1200 + 34 = 1234

nums = [2, 7, 4]
k = 181
temp = []
combined_string = ''.join(map(str, nums))
digit = int(combined_string) + k

number_str = str(digit)

for i in number_str:
    temp.append(i)
integer_list = [int(x) for x in temp]
print(integer_list)
