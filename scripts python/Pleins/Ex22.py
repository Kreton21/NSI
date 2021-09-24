a=int(input("Valeur de a ?")) 
b=int(input("Valeur de b ?")) 
while a!=b and b!=0: 
    d=abs(b-a)
    b=a 
    a=d 
print("pgcd=",d) 
if d==1: 
    print("Les deux entiers sont premiers entre eux.") 