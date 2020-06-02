l=[]
for i in range(int(input())):
    l.append(int(input()))
for i in range(len(l)):
    l1=l[i:]
    if max(l1) ==l[i]:
        print(l[i],end=' ')
