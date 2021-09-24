from turtle import *
color('red')
speed(0)
pos()
i=0
while True:
    i+=1
    forward(100)
    right (70)
    if abs(pos())<1:
        break
done()
