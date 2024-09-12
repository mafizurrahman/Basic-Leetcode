arr = [1,2,34,3,4,5,7,23,12]
new = []
for i in range(len(arr)-2):
    new.append([arr[i],arr[i+1],arr[i+2]])
check = 0
for i in new:
    for j in range(len(i)):
        # print(i)
        if i[j] % 2 != 0 and i[j+1] % 2 != 0 and i[j+2] % 2 != 0 :
            print(i)
            check += 1
            break
        break


if check == 0:
    print("false")



# print(new)

