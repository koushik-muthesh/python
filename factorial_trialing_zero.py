import math
for i in range(int(input())):
    n=int(input())
    c=0
    l=[]
    k=5
    while(len(l)<5):
        for j in range(1,11):
            a=math.factorial(j)
            while(j/k>=1):
                c+=int(j/k)
                k+=5
            if c==n:
                l.append(j)
    print(5)
    l.sort()
    print(l)
