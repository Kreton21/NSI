import random as rand

pari=int(input("Pari de de  \n"))
for i in range(pari):
    d=rand.randint(0,6)
    print("De",i,"=",d)
    # if d == 6