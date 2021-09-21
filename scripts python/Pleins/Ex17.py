import random as rand
pari=int(input("Pari de de  \n"))
for i in range(pari):
    d=rand.randint(1,6)
    print("De",i,"=",d)
    if d == 6:
        print("Win apres",i+1,"essaies")
        break
    elif i>pari:
        print("lose")