v={"Durand" : 13 , "Dupont" : 15 , "Dupond" : 17 , " Martin " : 20 }

def Nmbrv(T):
    c=0
    for i in T:
        c+=T[i]
    return c
def mv(T):
    mvp=0
    j=""
    for i in T:
        if T[i] > mvp:
            j = i
            mvp=T[i]
    return j


print(mv(v))