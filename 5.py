lst = [12, 3, 4, 10]
if len(lst) > 1:
    lst = [lst[-1]] + lst[:-1]
print(lst)
...
lst = [1]
if len(lst) > 1:
    lst = [lst[-1]] + lst[:-1]
print(lst)
...
lst = []
if len(lst) > 1:
    lst = [lst[-1]] + lst[:-1]
print(lst)
...
lst = [12, 3, 4, 10, 8]
if len(lst) > 1:
    lst = [lst[-1]] + lst[:-1]
print(lst)
...

def it1(lst):
    if len(lst) > 1:
        lst = [lst[-1]] + lst[:-1]
    return lst

print(it1([12, 3, 4, 10]))
print(it1([1]))
print(it1([]))
print(it1([12, 3, 4, 10, 8]))
...
