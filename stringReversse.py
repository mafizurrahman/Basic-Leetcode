list1 = ["Shogun","Tapioca Express","Burger King","KFC"]
list2 = ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]

index = []
name = []

for i in range(len(list1)):
    for j in range(len(list2)):
        if list1[i] == list2[j]:
            add = i + j
            index.append(add)
            name.append(list1[i])

# Find the lowest index value
lowest_index = min(index)

# Create a list to store names with the lowest index
lowest_index_names = [name[i] for i, idx in enumerate(index) if idx == lowest_index]

# Print multiple names if they share the same lowest index value
if len(lowest_index_names) > 1:
    print("Names with the Same Lowest Index Value:")
    print(lowest_index_names)
else:
    print("Name with the Lowest Index Value:")
    print(lowest_index_names[0])
