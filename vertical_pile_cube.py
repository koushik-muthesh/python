#t=int(input())
for i in range(int(input())):
    n=int(input())
    s=input().split()[0:n]
    l=[int(i) for i in s]
    a,b=l[0],l[-1]
    l.remove(l[0])
    l.pop()
    z=0
    for i in l:
        if i>=a or i>=b:
            z=z+1
    if z==0:
        print("YES")
    else:
        print("No")
