L=[3,5,2,3,6,3,4]
x=0
for i in range(len(L)):
    x += L[i]
print(x/len(L))


def moy(M):
    return sum(M)/len(M)