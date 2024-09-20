#num = int(input("Введіть число: "))
#q = num // 1000
#w = (num % 1000) // 100
#e = (num % 100) // 10
#r = num % 10
#print(q)
#print(w)
#print(e)
#print(r)
#...
number = int(input("число: "))
q, remainder = divmod(number, 1000)   # Отримуємо тисячі та залишок
w, remainder = divmod(remainder, 100)  # Отримуємо сотні та залишок
e, r = divmod(remainder, 10)  # Отримуємо десятки та одиниці
print(q)
print(w)
print(e)
print(r)
...
