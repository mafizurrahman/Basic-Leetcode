s = "egg"
t = "adl"
store = {}
store1 = {}

# Check if the strings have the same length
if len(s) != len(t):
    print("false")
else:
    for i in range(len(s)):
        # Check if s[i] is already mapped to a different character in t
        if s[i] in store and store[s[i]] != t[i]:
            print("false")
            break
        # Check if t[i] is already mapped to a different character in s
        if t[i] in store1 and store1[t[i]] != s[i]:
            print("false")
            break
        store[s[i]] = t[i]
        store1[t[i]] = s[i]
    print("true")
