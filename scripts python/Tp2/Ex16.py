M=[1,2,3,4,5,6,78,9,10]
def pimp(T):
    x=0
    for i in range (0,len(T)):
        if T[i]%2==0:
            x+=1
    X=[0]*x
    x=0
    for i in range(0,len(T)):
        if T[i]%2==0:
            X[x]=T[i]
            x+=1
    return X

print(pimp (M))