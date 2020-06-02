max1=0
chess=[]
st=[]
c=0
l1=[]
l2=[]
for i in range(1,9):
    l=[]
    for j in range(65,73):
        l3=[]
        s2=chr(j)+str(i)
        l3.append(s2)
        l.append(l3)
    chess.append(l)

s=input()
for i in range(0,len(s),2):
    s1=s[i]+s[i+1]
    st.append(s1)
for i in range(len(st)):
    for j in range(8):
        for k in range(8):
            a=chess[j]
            if a[k][0]==st[i]:
                if j+2<8 and k+1<8:
                    chess[j+2][k+1].append(1)
                    
                if j+2<8 and k-1>=0:
                    chess[j+2][k-1].append(1)
                    
                if j+1<8 and k+2<8:
                    chess[j+1][k+2].append(1)
                    
                if j-1>=0 and k+2<8:
                    chess[j-1][k+2].append(1)
                    
                if j-2>=0 and k+1<8:
                    chess[j-2][k+1].append(1)
                    
                if j-2>=0 and k-1>=0:
                    chess[j-2][k-1].append(1)
                    
                if j+1<8 and k-2>=0:
                    chess[j+1][k-2].append(1)
                    
                if j-1>=0 and k-2>=0:
                    chess[j-1][k-2].append(1)
#for i in chess:
 #   print(i)

for i in chess:
    for j in i:
        z=len(j)
        l2.append(z)
        if len(j)>1:
            c+=1
        if z>max1:
            max1=z
            l1=j
#print(l2)
#print(l1)

print(64-c)
l2.sort(reverse=True)
if l2[0]==l2[1]:
    print(-1)
else:
    print(l1[0])
