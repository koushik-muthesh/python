t=int(input())
for i in range(t):
    s=input().split()
    l=[int(i) for i in s]
    for j in range(len(l)):
        l1=l[j:]
        if len(l1)==0:
            l.append(-1)
        else:
            if j<max(l1):
                print(l1,max(l1))
                l[j]=max(l1)
            
    #print(l)
