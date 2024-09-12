candyType = [6,6,6,6]

c = len(candyType)
n = c/2

d = set(candyType)

# print("types of candy available: ", len(d))
#
# print("total he can get", n)

if len(d) <= n:
    print(len(d))
else:
    print(n)