from random import * #Importer la librairie random pour l'aleatoire
global Cmax #Creer une variable globale Cmax
Cmax=4  #Que lon va mettre a 4

def genererCombinaison(c,n,m): #Fonction qui va creer une combinaison de n chiffres entre 1 et m couleurs
  for i in range (n):
    c[i]=randrange(1,m)

def saisirCombinaison(c,n,m): #Fonction qui va creer une combinaison de n chiffres faite par l'utilisateur
    while True: #Boucle qui verifie l'input de lutilisateur
      inp=input("Try \n")
      if len(inp)!=n:
        print ("Longueur differente de",n)
      else:
        break
    for i in range(len(inp)): #Transforme l'input en combinaison
        c[i]=int(inp[i])

def afficherCombinaison(c,n): #Fonction qui va afficher la combinaison stocke dans la memoire sous c
  print(c)

def testCombinaison(): #Fonction qui deffinit les variables n,m,c (Combinaison de la machine) et d (Combinaison de l'utilisateur) 
  n=4
  m=6
  c=[0]*Cmax
  d=[0]*Cmax
  genererCombinaison(c,n,m)
  afficherCombinaison(c,n)
  saisirCombinaison(d,n,m)
  afficherCombinaison(d,n)
testCombinaison()