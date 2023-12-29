my_list = [2, 3, 4, {2, 3}]

# adds each element to existing list
my_list.extend([5, 6, 7])
print(my_list)

# Appends as it is
my_list.append([8, 9])
print(my_list)

# clone creates a deep copy of the list
clone = my_list.copy()
print(clone)

clone.extend([10, 11])
my_list.extend([12, 13])

print("clone: ", clone)
print("my_list: ", my_list)
