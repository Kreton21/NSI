import sys
import time as lethym

print("Formidable Area Calculator")
print("F.A.C Alexandru™")
print("Enter a:")
a=int(input())
print("Enter b:")
b=int(input())
print("Compiling answer:")

an = ["[■□□□□□□□□□]/","[■■□□□□□□□□]\\", "[■■■□□□□□□□]/", "[■■■■□□□□□□]\\", "[■■■■■□□□□□]/", "[■■■■■■□□□□]\\", "[■■■■■■■□□□]/", "[■■■■■■■■□□]\\", "[■■■■■■■■■□]/", "[■■■■■■■■■■]\\"]

for i in range(len(an)):
    lethym.sleep(0.4)
    sys.stdout.write("\r" + an[i % len(an)])
    sys.stdout.flush()

print("\n")

print("Area =",a*b)