#   ___  _                          _            _     
#  / _ \| |                        | |          ( )    
# / /_\ \ | _____  ____ _ _ __   __| |_ __ _   _|/ ___ 
# |  _  | |/ _ \ \/ / _` | '_ \ / _` | '__| | | | / __|
# | | | | |  __/>  < (_| | | | | (_| | |  | |_| | \__ \
# \_| |_/_|\___/_/\_\__,_|_| |_|\__,_|_|   \__,_| |___/ and Eliez
    # Incredible Mastermind ™                                     
# ======================       
import random as rand

def startup():
    global a
    global b
    print("PS: La combinaison chiosie par la machine est affiche car le logiciel est en mode developpement")
    print("1 = 4 chiffres, 4 couleurs et 20 essais")
    print("2 = 6 chiffres, 6 couleurs et 10 essais")
    print("3 = Personalise")
    a=int(input("Entrer la difficulte du jeu:\n"))
    if a == 1:
        a=4
        b=20
    elif a == 2:
        a=6
        b=10
    else: a=int(input("Entrez la taille de combinaison \n"));b=int(input("Entrez le nombre d'essais \n"))
    A=[0]*a
    for i in range(len(A)):
        A[i]=rand.randrange(1,len(A))
    return(A)

def tryy():
    B=[0]*a
    print("Entrez une combinaison de",a,"chiffres \n")
    c=input()
    for i in range(len(c)):
        B[i]=int(c[i])
    return(B)

def game(A,B):
    global b
    while A != B and b>0:
        C=""
        D=[0]*a
        for i in range(a):
            D[i]=A[i]
        for i in range(a):
            if D[i]==B[i]:
                C+="#"
                D[i]=-1
        for i in range(a):
            for j in range(a):
                if B[i]==D[j]:
                    C+="o"
                    D[j]=-1
                    break

        print(A,"Combinaison choisie par la machine a enlever a la version finale")
        print(B,"Votre combinaison")
        print(b,"nombre d'essai restants")
        print(C)
        B=tryy()
        b=b-1
#    print (a)



game(startup(),tryy())
print("Bravo")
