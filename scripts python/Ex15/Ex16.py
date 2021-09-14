age=int(input("Age \n"))
stud=int(input("Anees d'etudes, -1 si pas de BAC \n"))
cup=int(input("Celibataire 1 ou 0 \n"))
kid=int(input("Nombre d'INFANTS \n"))
car=int(input("Voiture 1 ou 0 \n"))
s=0

if age <= 40:
    s+=1
if stud < 2:
    s+=1
if cup == False:
    s+=1
if kid >1:
    s+=1
if car == True:
    s+=1
if s >= 5:
    print("Client tres probable")
elif s==4 or s==3:
    print("Client probable")
elif s==0:
    print("Clien nul")
else:
    print("Client peu probable")