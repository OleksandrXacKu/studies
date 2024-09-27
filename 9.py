lst_1 = [0, 1, 0, 12, 3]
lst_2 = [0]
lst_3 = [1, 0, 13, 0, 0, 0, 5]
lst_4 = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]
def z(lst):
    no_zero = [x for x in lst if x !=0]
    zero = [0] * (len(lst) - len(no_zero))
    return no_zero + zero
# print(z(lst_1))
# print(z(lst_2))
# print(z(lst_3))
# print(z(lst_4))
print(f"{lst_1}->{z(lst_1)}",f"{lst_2}->{z(lst_2)}",f"{lst_3}->{z(lst_3)}",f"{lst_4}->{z(lst_4)}",sep="\n" )

