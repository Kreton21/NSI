a=int(input("a -"))
b=int(input("b -"))
if a>0 and b>0:
    m, n = a, b
    while m>=b:
        m,n =m-b,n+1
    print('m =',m,"n=",n)