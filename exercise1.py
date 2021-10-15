a=int(input("Значение первого числа"))
b=int(input("Значение второго числа"))
c=int(input("Значение третьего числа"))
f = a+b
g = a+c
h = b+c
if a+b>b+c:
    if a+b>a+c:
        print("наибольшая сумма у a+b",f)
    elif a+b<a+c:
        print("наибольшее число у a+c",g)
elif a+b<b+c:
    if a+c<b+c:
        print("наибольшая сумма у b+c",h)
else:
    print("суммы равны")
