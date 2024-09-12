s1 = "CODE"
s2 = "CODE"
s3 = ""

i = 0
j = 0

while i < len(s1) and j < len(s2):
    if s1[i] != s2[j]:
        print( "no" )
        break

    if s1[i] == s2[j]:
        if s1[i] not in s3:
            s3 += s1[i]
            i += 1
            j += 1
        else:
            break



generated_string = ""
if len(s1) > len(s3):
        while len(generated_string) < len(s1):
            generated_string += s3

        if generated_string == s1:
            print(f"You can generate string2 from string1 by repeating '{s3}'.")
        else:
            print("You cannot generate string2 from string1.")

else:
    while len(generated_string) < len(s3):
        generated_string += s1

    if generated_string == s3:
        print(f"You can generate string2 from string1 by repeating '{s1}'.")
    else:
        print("You cannot generate string2 from string1.")
# print(s3)
# # print(s3)
# s4 = ""
# for i in range(len(s1)):
#     s4 += s3
#     # print(i, " ", s4)
#     if s4 == s1:
#         break
# return s3


