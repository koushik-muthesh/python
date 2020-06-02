n=int(input())
l=[]
for i in range(n+1):
    l.append('0')
l1=[]
a=0
for i in range(1,n+1):
    for j in range(1,n+1):
        if i*j<=n:
            if l[i*j]=='1':
                l[i*j]='0'
            elif l[i*j]=='0':
                l[i*j]='1'
            print(i*j)
print(l)
            
