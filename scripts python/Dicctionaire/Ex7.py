notes={"a":[1,2,3,4],"b":[4,3,3,4],"c":[1,223,3,4]}

def mm(T):
    me=""
    mme=0
    for i in T:
        if sum(T[i])/len(T[i]) > mme:
            mme = sum(T[i])/len(T[i])
            me=i
    return me

print (mm(notes))
        