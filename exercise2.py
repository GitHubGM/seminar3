try:
    n=int(input("Ввудите значение n"))
    sum=0
    i=1
    while i<=n:
        sum=i+sum
        i=i+1
    print("сумма",sum)
except:
    print("Error")
    exit()    
