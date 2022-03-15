import os as o

def genererT(n):
    T=[0]*11
    for i in range (11):
        T[i]=str(n)+"*"+str(i)+"="+str(n*i)+"\n"
    return T
f = open("tablesMult.txt", "w")

f.writelines(genererT(5))
f.close()