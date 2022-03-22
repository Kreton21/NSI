import csv
from collections import OrderedDict
import json
f=open("/home/kreton/Documents/code/NSI/scripts python/CSV/notes.csv",encoding="utf8")
table=list(csv.DictReader(f,delimiter=","))
print(table)

#def convert(T):
#    R=json.loads(json.dumps(T))
#    return R

def correct(T):
    for i in T:
        for j in i:
            if j !="Nom":
                i[j]=int(i[j])
    return(T)

def moy(dico):
    somme=0
    n=0
    for e in dico:
        if e != "Nom":
            somme=somme+dico[e]
            n=n+1
    m=somme/n
    dico["Moyenne"]=m
    return dico
a = correct(table)
Tmoy=[moy(dico) for dico in table]
#print(Tmoy)


t1=[ligne["Nom"] for ligne in table]
print(t1)
t2=[ligne["Anglais"] for ligne in table if float(ligne["Anglais"])>10]
print(t2)
t3=[ligne["Nom"] for ligne in table if float(ligne["Maths"])>18 and float(ligne["NSI"])>10]
print(t3)
t4=[{"Nom":ligne["Nom"],"Anglais":ligne["Anglais"]} for ligne in table]
print(t4)
t5=[{"Nom":ligne["Nom"],"Math+1":ligne["Maths"]+1 if ligne["Maths"]<20 else ligne["Maths"]} for ligne in table]
print(t5)
t6=[{"Nom":ligne["Nom"],"Moy":ligne["Moyenne"]} for ligne in table]
print(t6)



