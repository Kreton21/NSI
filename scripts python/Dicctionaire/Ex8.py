from math import *
clav = [ [ ' a ' , ' z ' , ' e ' , ' r ' , ' t ' , ' y ' , ' u ' , ' i ' , ' o ' , ' p ' ] , [ ' q ' , ' s ' , ' d ' , ' f ' , ' g ' , ' h ' , ' j ' , ' k ' , ' l ' , 'm' ] , [ '< ' ,
'w ' , ' x ' , ' c ' , ' v ' , ' b ' , ' n ' , ' , ' , ' ; ' , ' : ' ] ]

def inverseCLav(T):
    D={}
    for i in range(len(T)):
        for j in range(len(T[0])):
            n=T[i][j]
            D[n]=(i,j)
    return D
def distance_touche(n,m, coord):
    N=coord[n]
    M=coord[m]
    dist=sqrt((N[0]-M[0])**2+(N[1]-M[1])**2)
    return dist
x=inverseCLav(clav)
print (x)
print(distance_touche(" a "," k ",x))