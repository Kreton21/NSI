v=True
a=int(input("Combien de quilles avec la 1er boule? \n"))
if a == 10:
    print("X")
elif a>10 or a<0:
    v=False
elif a<10 and a>0:
    b=int(input("Combien de quilles avec la 2eme boule? \n"))
    if b+a > 10:
        v=False
    elif b+a == 10:
        print("/")
    else:
        print("Vous avez fait tomber",a+b,"quilles")
if v != True:
    print("!")