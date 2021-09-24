from turtle import *
a=int(input())
while True:
    forward (90)
    left(360/a)
    if abs(pos())!=0:
        break
done()