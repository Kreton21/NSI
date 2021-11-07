L=[2,4,6,8,10,12,14,16]
def f(L):
    for i in range(len(L)):
        L[i]=L[i]*2
    return L
print(f(L))