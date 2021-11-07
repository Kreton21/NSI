L=[0]*int(input())
for i in range (0,len(L)):
    L[i]=int(input("ta meree"))

def somme(L):
    x=0
    for i in range (0,len(L)):
        x+=L[i]
    return x

print(somme(L))