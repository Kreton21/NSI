P=[2,5,59,5,78,58,5,7]
def p0cc(L,x):
    y=0
    o=0
    for i in range(0,len(L)):
        if L[i]==x:
            y+=1
    u=[0]*y
    for i in range (0,len(L)):
        if L[i]==x:
            u[o]=i
            o+=1
    if o==0:
        return -1
    else:return u[0]
print(p0cc(P,5))