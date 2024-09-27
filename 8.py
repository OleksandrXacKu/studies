def a_t(lst):
    if len(lst) == 0:
        return 0
    return sum(lst[i] for i in range(0, len(lst), 2)) * lst[-1]

lst_1 = [0, 1, 7, 2, 4, 8]
lst_2 = [1, 3, 5]
lst_3 = [6]
lst_4 = []
print(a_t(lst_1))
print(a_t(lst_2))
print(a_t(lst_3))
print(a_t(lst_4))