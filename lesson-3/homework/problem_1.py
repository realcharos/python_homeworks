lst = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
element = 5
index = 2
number = 3
sublist = [1, 5, 9]

count = lst.count(element)
print(count)

total = sum(lst)
print(total)

max_value = max(lst)
print(max_value)

min_value = min(lst)
print(min_value)

exists = element in lst
print(exists)

first = lst[0] if lst else None
print(first)

last = lst[-1] if lst else None
print(last)

sliced = lst[:3]
print(sliced)

reversed_lst = lst[::-1]
print(reversed_lst)

sorted_lst = sorted(lst)
print(sorted_lst)

unique_lst = list(set(lst))
print(unique_lst)

lst.insert(index, element)
print(lst)

index_of_element = lst.index(element) if element in lst else -1
print(index_of_element)

is_empty = len(lst) == 0
print(is_empty)

even_count = sum(1 for x in lst if x % 2 == 0)
print(even_count)

odd_count = sum(1 for x in lst if x % 2 != 0)
print(odd_count)

list2 = [7, 8, 9]
concatenated = lst + list2
print(concatenated)

sublist_exists = str(sublist)[1:-1] in str(lst)
print(sublist_exists)

if element in lst:
    lst[lst.index(element)] = 99
print(lst)

second_largest = sorted(set(lst), reverse=True)[1] if len(set(lst)) > 1 else None
print(second_largest)

second_smallest = sorted(set(lst))[1] if len(set(lst)) > 1 else None
print(second_smallest)

even_numbers = [x for x in lst if x % 2 == 0]
print(even_numbers)

odd_numbers = [x for x in lst if x % 2 != 0]
print(odd_numbers)

length = len(lst)
print(length)

copy_lst = lst[:]
print(copy_lst)

mid = lst[len(lst)//2] if len(lst) % 2 != 0 else lst[len(lst)//2-1:len(lst)//2+1]
print(mid)

max_sublist = max(sublist) if sublist else None
print(max_sublist)

min_sublist = min(sublist) if sublist else None
print(min_sublist)

if 0 <= index < len(lst):
    del lst[index]
print(lst)

is_sorted = lst == sorted(lst)
print(is_sorted)

repeated = lst * number
print(repeated)

merged_sorted = sorted(lst + list2)
print(merged_sorted)

indices = [i for i, x in enumerate(lst) if x == element]
print(indices)

rotated = lst[-1:] + lst[:-1]
print(rotated)

range_list = list(range(1, 11))
print(range_list)

sum_positive = sum(x for x in lst if x > 0)
print(sum_positive)

sum_negative = sum(x for x in lst if x < 0)
print(sum_negative)

is_palindrome = lst == lst[::-1]
print(is_palindrome)

nested = [lst[i:i+3] for i in range(0, len(lst), 3)]
print(nested)

seen = set()
unique_in_order = [x for x in lst if not (x in seen or seen.add(x))]
print(unique_in_order)
