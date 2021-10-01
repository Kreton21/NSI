def bisex(a):
    if a%4==0:
        print("Anee bisextile")
        return True
    else:
        print ("Anee invalide ou pas bisextile")
        return False
def nj(a):
    if bisex(a):
        return 366
    else: return 365
def nbjm(a,b):
    if b == 2 and bisex(a)==True:
        return 29
    elif b==2:
        return 28
    if b%2==0:
        return 30
    else:return 31
def fcp(a,b,c,d,e,f):
    an=abs(a-d)
    ann=(an*365)+(an//4)
    mn=abs(b-e)
    mnn=0
    if (b>=2 and d<=2) and bisex(a)==True:
        mnn+=29
    elif (b>=2 and d<=2) and bisex(a)==False:
        mnn+=28
    elif (b<=1 and d>=3) and bisex(b)==True:
        mnn+=29
    elif (b<=1 and d>=3) and bisex(b)==False:
        mnn+=28
    for i in range(mn):
        if i%2==0:
            mnn+=30
        else:mnn+=31
    jn=abs(c-f)
    return ann+mnn+jn
print(fcp(2020,3,10,2021,3,12))