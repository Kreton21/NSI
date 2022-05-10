T=[1,2,3,4,5,6]
C=[4,2,5,7,1,4,4]

def tri(T):
    Z=[0]*len(T)
    for i in range (len(T)):
        V=T[i]
        j=i
        while j>0 and V<Z[j-1]:
            Z[j]=Z[j-1]
            j=j-1
        Z[j]=V
    return Z
def freq(T):
    Z = tri(T)
    max=1
    for i in range(len(Z)):
        C=Z[i]
        if Z[i-1] == C:
            max+=1
    return max

print(freq(C))
    
print(tri(C),C)