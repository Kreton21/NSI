def I(n):
    I=[[0]*n for i in range(n)]
    for i in range (n):
        I[i][i]=1
    return I


T=[[0]*10 for i in range(10)]
for i in range(10):
    T[i][i]=1
#print(T)

print(I(10))