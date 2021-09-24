from turtle import *
color('red')
speed(0)
pos()
while True:
    forward(100)
    left (90)
    if abs(pos())<1:
        break
done()

