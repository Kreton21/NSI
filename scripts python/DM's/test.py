import turtle as t
t.fillcolor("red")
def itoile():
    t.up()
    t.begin_fill()
    for i in range(5):
        t.forward(20)
        t.right(144)
    t.end_fill()

itoile()