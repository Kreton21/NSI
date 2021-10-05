def noz(L):
    n=len(L)
    s=0
    for i in range(0,n,1):
        if L[i]!=0:
            s+=1
    return s
print(noz(L))