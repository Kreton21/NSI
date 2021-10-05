#   ___  _                          _            _     
#  / _ \| |                        | |          ( )    
# / /_\ \ | _____  ____ _ _ __   __| |_ __ _   _|/ ___ 
# |  _  | |/ _ \ \/ / _` | '_ \ / _` | '__| | | | / __|
# | | | | |  __/>  < (_| | | | | (_| | |  | |_| | \__ \
# \_| |_/_|\___/_/\_\__,_|_| |_|\__,_|_|   \__,_| |___/
    # Incredible Europe Flag Designer ™                                     
# ======================                               
import turtle as t #Importer le module turtle de python
t.fillcolor("#003399") #Valeurs precises du fond du drapeau
t.up() #Raccourcit de pen_up qui leve le stylo
t.hideturtle() #Cacher la tortue qui dessine   
t.speed(0) #Mettre la vitesse de la tortue au maximum
# ======================
# Faire le fond bleu du drapeau
t.goto(-185,185) #Aller au coordonees -185 x et 185 y
t.begin_fill() #Commencer la fonction fill() Voir https://docs.python.org/3/library/turtle.html#turtle.filling
for i in range(4): #Boucle de construction du fond du drapeau
    t.forward(400) #Faire avancer la tortue de 400 px 
    t.right(90) #Faire tourner la tortue de 90° vers la droite
t.end_fill() #Finir la fonction fill() et remplir le carre en bleu
# ======================
def itoile(): #Creer la fonction qui va se charger de dessiner une etoile
    t.seth(0) #Raccourcit de Set heading qui (en mode normal et non pas logo voir https://docs.python.org/3/library/turtle.html#turtle.seth) va mettre la direction de la tortue vers l'est
    t.begin_fill() #Demmarage de la fomction fill() pour remplir l'etoile
    for i in range(5):# Boucle de construction de l'etoile
        t.forward(35) # Avamcer de 35px (A changer pour modifier la taille des etoiles)
        t.right(144)  # Faire tourner la tortue vers la droite de 144 degrees
    t.end_fill() #Fin de la fonction fill() et coloriage des etoiles (A noter que pour certaines versions de pyhon/turtle, l'interieur des etoiles ne se remplit pas correctement)
# ======================
t.fillcolor("#ffcc00") #Valeurs precises des etoiles
a=0 #Creer un conteur qui va tenir compte des degrees parcourus par la tortue
for i in range(12): # La boucle de construction des 12 etoiles du drapeau
    t.home() #La fonction home() est une combinaison de la fonction goto(0,0) et seth(0) qui ramene la tortue a la position initiale.
    t.left(a) #Fait tourner la tortue de a degrees a partir de 0 (a va augmenter de 360/12 car il y as douze etoiles dans le drapeau)
    t.forward(125) #Distance des etoiles du centre (A changer pour modifier la distance des etoiles du centre)
    itoile() #Appele la fonction de construction de l'etoile (voir itoile)
    a+=30 # Roujouter 30 degrees au conteur d'angle
# ======================
t.exitonclick() #Ne pas quitter le programme une fois la construction finie