T=[[0]*5 for i in range (3)]
T[2][3]=45
print (T)

def maxL(T,n):
    maxi = T[n][0]
    for i in range (len(T[n])):
        if T[n][i] > maxi:
            maxi=T[n][i]
    return maxi
def maxC(T,k):
    maxi = T[0][k]
    for i in range(len(T)):
        if T[i][k]>maxi:
            maxi=T[i][k]
    return maxi
print(maxC(T,3))