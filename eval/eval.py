clavier=(
    ('1','2','3'),
    ('4','5','6'),
    ('7','8','9')

)
def inverseClavier(T):
    a={}
    i=0
    for e in range( len (T)):
        for f in range(len(T[e])):
            a[i]={str(T[e][f]):int(f+e*10)}
            i+=1
    return a
print ()
a = inverseClavier(clavier)
print(a[int('2')-1]['2'])
print (inverseClavier(clavier))

def dist(a,b,coord):
    xa=0
    ya=0
    xb=0
    yb=2
    if len(str(coord[int(a)-1][a])) == 1:
        xa=0
        xy=int(a)
    else:xa=abs(int(str(coord[int(a)-1][a])[1]));ya=int(str(coord[int(a)-1][a])[0])
    if len(str(coord[int(b)-1][b])) == 1:
        xb=0
        xy=int(b)
    else:xb=abs(int(str(coord[int(b)-1][b])[1]));yb=int(str(coord[int(b)-1][b])[0])
    return (abs(xa-xb+ya-yb))

print (dist('1','3',inverseClavier(clavier)))