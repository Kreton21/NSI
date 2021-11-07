def d(a,b):
    if a<=b:
        for i in range(a,b+1):
            a+=i**5
            print ("a",a)
    return(a)
def e(n):
    if n==0:
        return True
    else:
        b=1
        for i in range(n):
            b=b*n
            print("b=",b)
        return b
def puissance(x,y):
    if y==0:
        return 0
    else:
        c=1
        for i in range(y):
            c=c*x
        return c
print(puissance(2,3))
