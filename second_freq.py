from collections import Counter as C
s=input()
c=C(s)
l=[]
c=sorted(c.items(),key=lambda x:x[1],reverse=True)
#c=sorted(c,key=lambda x:x[0],reverse=True)
c=sorted(c,key=lambda x:x[1],reverse=True)
if c[0][1]==1:
    print("No frequent Characters")
else:
    for i in range(len(c)):
        if c[0][1]==c[i][1]:
            l.append(c[i])
if l==[]:
    print(c[1][1])
else:
    l.sort()
    print(l[0][1])

    
            
