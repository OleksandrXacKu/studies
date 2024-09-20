num = int(input("введіть число :"))
remainder = num
t, remainder = divmod(remainder, 10000)
r, remainder = divmod(remainder, 1000)
e, remainder = divmod(remainder, 100)
w, remainder = divmod(remainder, 10)
q = remainder
print(q,w,e,r,t)
...
