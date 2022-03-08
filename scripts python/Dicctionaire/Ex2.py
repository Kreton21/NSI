T=[1,2,3,4,5,1,1,1]
f=open("/home/alexandru/Alexandru/NSI/scripts python/Dicctionaire/ltdme80j-p.txt")
text=f.read().split()
f.close()
def occurence (T):
    D={}
    for i in T:
        if i in D:
            D[i]+=1
        else: D[i]=1
    return D
# print (T)
texte=occurence(text)

def plusfreq(T):
    R={}
    for i in T:
        for j in i:
            if j in R:
                R[j]+=1
            else :R[j]=1
    return R
def plusfreq2(T,k):
    R={}
    for i in T:
        if len(i)==k:
            if i in R:
                R[i]+=1
            else :R[i]=1
    return R
n=sorted(plusfreq2(text,7).items(), key=lambda item: item[1])
m=sorted(plusfreq(texte).items(), key=lambda item: item[1])
# print (m)
print(n)