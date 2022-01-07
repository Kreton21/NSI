def encodeAndPrint(n):
    while n//2 != 0:
        r=n%2
        mot=r+mot
        n=n//2
        print(mot)
def encodeAndPrint2(n):
    mot=""
    while n!=0:
        r=n%2
        mot=str(r)+mot
        n=n//2
    for i in range(8-len(mot)):
        mot=str(0)+mot
    print(mot)