n = int(input("Enter The Number: "))

count = 0

for i in range(n):
    if(n % 2 == 0):
            n = n / 2
            # print(n)
            count += 1


    else:
        n = n-1
        count += 1
        if n == 0:
            break



print("count", count)
