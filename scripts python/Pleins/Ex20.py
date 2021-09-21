from math import sqrt
n = int(input())
pf = 0
if(n >= 2):
    for i in range(2, int(sqrt(n)) + 1):
        if (n % i == 0):
            pf = 1
            break
    if (pf == 0):
        print("true")
    else:
        print("false")
else:
    print("false")