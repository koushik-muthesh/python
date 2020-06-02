n=int(input())
l=[]
l1=[]
p=[]
for i in range(n):
    l.append(int(input()))
for i in range(n):
    l1.append(int(input()))

for i in range(min(l),max(l1)):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        if i!=1:
            p.append(i)
#print(p)
for k in range(n):
    c=0
    l3=[]
    l2=[]
    for w in range(l[k],l1[k]+1):
        if w!=1:
            l2.append(w)
    #print(l2)
    for z in range(len(p)):
        for x in range(len(p)):
            if (p[z]*p[x]) in l2:
                c=c+1
                if (p[z]*p[x]) not in l3:
                    l3.append(p[z]*p[x])
                    c=c+1
    print(len(l3))








        
'''for k in range(n):
    c=0
    for i in range(len(p)):
        for j in range(len(p)):
            if p[i]*p[j] >=l[k] and p[i]*p[j]<=l1[k]:
                c=c+1
                #print(i*j)

    print(c)'''
                
