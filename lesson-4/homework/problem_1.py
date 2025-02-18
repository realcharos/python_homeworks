list1 = [1, 1, 2]
list2 = [2, 3, 4]

unique1 = [x for x in list1 if x not in list2]
unique2 = [x for x in list2 if x not in list1]

result = unique1 + unique2
print(result)
