lst = [1, 2, 3, 4, 5, 6]
if len(lst) == 0:
    result = [[], []]
else:
    mid = (len(lst) +1) // 2
    first_part = lst[:mid]
    second_part = lst[mid:]
    result = [first_part, second_part]
print(result)
...
lst = [1, 2, 3]
if len(lst) == 0:
    result = [[], []]
else:
    mid = (len(lst) +1) // 2
    first_part = lst[:mid]
    second_part = lst[mid:]
    result = [first_part, second_part]
print(result)
...
lst = [1, 2, 3, 4, 5]
if len(lst) == 0:
    result = [[], []]
else:
    mid = (len(lst) +1) // 2
    first_part = lst[:mid]
    second_part = lst[mid:]
    result = [first_part, second_part]
print(result)
...
lst = [1]
if len(lst) == 0:
    result = [[],[]]
else:
    mid = (len(lst) +1) // 2
    first_part = lst[:mid]
    second_part = lst[mid:]
    result = [first_part, second_part]
print(result)
...
lst = []
if len(lst) == 0:
    result = [[], []]
else:
    mid = (len(lst) +1) //2
    first_part = lst[:mid]
    second_part = lst[mid:]
    result = [first_part, second_part]
print(result)
...

#def it1_list(lst):
    #if len(lst) == 0:
        #return [[], []]
    #it2_list = (len(lst) +1) // 2
    #return [lst[:it2_list], lst[it2_list:]]
#print(it1_list([1, 2, 3, 4, 5, 6]))
#print(it1_list([1, 2, 3]))
#print(it1_list([1]))
#print(it1_list([]))
#...