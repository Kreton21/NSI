import sys
import time as lethym
import math
def start():
    print("Formidable Fat Factor")
    print("Enter 1 for Height")
    print("Enter 2 for Mass")
    ch=int(input())
    if ch == 1:
        ty=1
        height(ty)
    elif ch == 2:
        ty=2
        print("debug")
        mass(ty)
    else:
        print("Veuillez entrer 1 ou 2")
        start()

def height(ty):
    print("Please enter height:")
    h=float(input())
    resl=18.5*h**2
    resh=25*h**2
    compil(resl,resh,ty)
def mass(ty):
    print("Please enter mass:")
    m=int(input())
    resl=m/18.5
    resh=m/25
    compil(resh,resh,ty)
def compil(resl,resh,ty):
    print("\r","Compiling please wait")
    an = ["[■□□□□□□□□□]/","[■■□□□□□□□□]\\", "[■■■□□□□□□□]/", "[■■■■□□□□□□]\\", "[■■■■■□□□□□]/", "[■■■■■■□□□□]\\", "[■■■■■■■□□□]/", "[■■■■■■■■□□]\\", "[■■■■■■■■■□]/", "[■■■■■■■■■■]\\"]
    for i in range(len(an)):
        lethym.sleep(0.4)
        sys.stdout.write("\r" + an[i % len(an)])
        sys.stdout.flush()
    print("\r")
    if ty == 1:
        print("Vous devez peser entre",round(resl),"et",round(resh),"Kg")
    if ty == 2:
        print("Vous devez etre entre",resl,"et",resh,"m")

start()
