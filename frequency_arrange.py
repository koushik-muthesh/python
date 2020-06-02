from collections import Counter as C
for i in range(int(input())):
    l=input().split()
    l1=C(l)
    #print(l1)
    l1=sorted(l1.items(),key=lambda x:x[1],reverse=True)
    #print(l1)
    for i in range(len(l1)-1):
        if l1[i][0]>l1[i+1][0]and l1[i][1]==l1[i+1][1]:
            temp=l1[i]
            l1[i]=l1[i+1]
            l1[i+1]=temp
    for i in l1:
        for j in range(i[1]):
            print(i[0],end=' ')
               
