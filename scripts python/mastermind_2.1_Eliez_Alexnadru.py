from random import*
global Cmax
Cmax=4

def genererCombinaison(c,n,m):
  c=[0]*n
  for i in range (n):
    c[i]=randrange(1,m+1)
  return c
def saisirCombinaison(c,n,m):
    c=[0]*n
    while True:
      inp=input("Try")
      if len(inp)!=n:
        print ("Longueur differente de",n)
      else:
        break
    for i in range(len(inp)):
        c[i]=int(inp[i])
    return c
def afficherCombinaison(c):
  x=[0]*len(c)
  for i in range (len(c)):
    if c[i]==-1:
      x[i]="BI"
    elif c[i]==-2:
      x[i]="MA"
  print(x)

def testCombinaison():
  n=4
  m=6
  c=[0]*Cmax
  d=[0]*Cmax
  genererCombinaison(c,n,)
  afficherCombinaison(c,n)
  saisirCombinaison(d,n,m)
  afficherCombinaison(d,n)

testCombinaison 

###################################
# code=[]
# code=genererCombinaison(code,4,4)
#print(code)
# copie=code
BIEN_PLACE=-1
MAL_PLACE=-2
##################################

def trouverbienplaces(copie,c):
  for i in range(len(c)):
    if c[i]==copie[i]:
      copie[i]=BIEN_PLACE


def position(valeur,c):
  for i in range (len(c)):
    if c[i]==valeur:
      return i
  return -1
# test=[2,1,4,4]

# position(1,test)


def trouvermalplace(copie,c):
  global codesecret
  for i in range(len(c)):
    a=position(c[i],codesecret)
    if a != -1 and copie[i]!=-2 and copie[i]!=-1:  
      copie[i]=MAL_PLACE

# comb=[]
# comb=saisirCombinaison(comb,4,4)
# trouverbienplaces(copie,comb)
# trouvermalplace(copie,comb)
# print("code secret=",code)
# afficherCombinaison(copie)

def copierCombinaison(src,dest):
  for i in range(len(src)):
    dest[i]=src[i]

#def etudiercode(c1,c2):
# a=[0]*4
# b=[1,3,41,1]
# copierCombinaison(b,a)
# print(a)  
codesecret=[]
def mastermind(n,m,maxcoups):
  global codesecret
  codesecret=genererCombinaison(codesecret,n,m)
  copie=[0]*n
  print(codesecret,"code")
  copierCombinaison(codesecret,copie)
  win=False;i=maxcoups
  while win==False and 0 < maxcoups:
    userimp=[]
    userimp=saisirCombinaison(userimp,n,m)
    if userimp==codesecret:
      win=True
      break
    copierCombinaison(codesecret,copie)
    trouverbienplaces(copie,userimp)
    trouvermalplace(copie,userimp)
    print(copie)
    print(codesecret)

mastermind(4,4,10)
# def saisirNiveau():
#   f=int(input("Entrez le chiffre du niveau choisi : 1-Novice      2-Pro      3-Killer"))
#   if f==1:
#      n=4
#      maxcoups=12
#   elif f==2:
#     n=5
#     maxcoups=15
#   else:
#     n=6
    
    
# def bienvenue(n,m,maxcoups):
#   print ("Bienvenue sur le Mastermind de Eliez et Alexandru \n Le principe du jeu est de trouver la combinaison produite par l'ordinateur.\n Selon le niveau que vous allez choisir entre Novice, Pro et Killer il y aura 4, 5 ou 6 chiffres à trouver.\n                                      ")




   

    
  
  