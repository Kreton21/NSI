def py(n):
    for i in range (n):
        print("  "*round(i/2),"*"*i)
    a=n

    for i in range (n):
        print("  "*round(a/2),"*"*a)
        a+=-1
py(50)