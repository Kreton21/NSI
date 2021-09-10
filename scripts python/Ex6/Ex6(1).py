import math
import random as ran

x=ran.randrange(1,20)
y=ran.randrange(1,20)
z=ran.randrange(1,20)

print(x,y,z)

a=z
z=y
y=x
x=a

print (x,y,z)
