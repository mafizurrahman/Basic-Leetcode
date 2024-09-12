nums = [1,2]
target = 8
new = []

# Find the indices of the target value in the nums list
for i in range(len(nums)):
    if target == nums[i]:
        new.append(i)

# Check if the length of new is equal to 1
if len(new) == 1:
    new.append(new[0])  # Add the element from new back into itself

# Check if there are at least two elements in new
if len(new) >= 2:
    new = [new[0], new[-1]]  # Keep only the first and last elements

# Check if new is empty and print [-1, -1] if it is
if not new:
    print("[-1, -1]")
else:
    print(new)
