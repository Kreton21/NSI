T=[[0]*2 for i in range (3)]
T[1][1]=45
T[2][1]=35

def somme(T):
    sum=0
    for i in range(len(T)):
        for j in range (len(T[i])):
            sum += T[i][j]
    return sum
print (somme(T))