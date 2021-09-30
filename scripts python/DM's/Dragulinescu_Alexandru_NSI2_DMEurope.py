#   ___  _                          _            _     
#  / _ \| |                        | |          ( )    
# / /_\ \ | _____  ____ _ _ __   __| |_ __ _   _|/ ___ 
# |  _  | |/ _ \ \/ / _` | '_ \ / _` | '__| | | | / __|
# | | | | |  __/>  < (_| | | | | (_| | |  | |_| | \__ \
# \_| |_/_|\___/_/\_\__,_|_| |_|\__,_|_|   \__,_| |___/
    # Incredible Europe Flag Designer ™                                     
# ======================                               
import turtle as t
t.fillcolor("#003399") #Valeurs precises du fond du drapeau
t.up()
t.hideturtle()
t.speed(0)
# ======================
t.goto(-185,185)
t.begin_fill()
for i in range(4):
    t.forward(400) 
    t.right(90)
t.end_fill()
# ======================
def itoile():
    t.seth(0)
    t.begin_fill()
    for i in range(5):
        t.forward(35)
        t.right(144)
    t.end_fill()
# ======================
t.fillcolor("#ffcc00") #Valeurs precises des etoiles
a=0
for i in range(12):
    t.home()
    t.left(a)
    t.forward(125)
    itoile()
    a+=30
# ======================
t.exitonclick()