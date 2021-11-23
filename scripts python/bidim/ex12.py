def tri(n):
    T=[[0]*n for i in range(n)]
    T[0][0]=1
    for i in range (1,len(T)):
        for j in range(len(T[i])):
            T[i][j]=T[i-1][j-1]+T[i-1][j]
    return T
print (tri(6))