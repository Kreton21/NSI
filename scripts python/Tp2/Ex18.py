
T=[1,2,3,4,5,6,7,245,9,14535630,11,12]
def renverse(T):
    for i in range(len(T)):
        print(T)
        for i in range(len(T)-1):
            if T[i] < T[i+1]:
                T[i],T[i+1]=T[i+1],T[i]
renverse(T)
