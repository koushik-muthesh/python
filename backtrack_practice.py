def Find(soln,prob,x,y):
    if x==n-1 and y==m-1:
        soln[x][y]=1
        return 1

    if x<n and y<n and x>=0 and y>=0 and prob[x][y]==0 and sol[x][y]!=1:
        sol[x][y]=1

        if Find(sol,prob,x+1,y)==1:
            sol[x][y]=1
            return 1
        if Find(sol,prob,x,y+1)==1:
            sol[x][y]=1
            return 1
        if Find(sol,prob,x-1,y)==1:
            sol[x][y]=1
            return 1
        if Find(sol,prob,x,y-1)==1:
            sol[x][y]=1
            return 1
        sol[x][y]=0
        return 0
    return 0

n,m=map(int,input().split())
prob=[]
sol=[]
for i in range(n):
    l=list(map(int,input().split()))[:m]
    prob.append(l)
for i in range(n):
    l1=[]
    for j in range(m):
        l1.append(0)
    sol.append(l1)

if Find(sol,prob,0,0)==0:
    print("False")
else:
    for i in sol:
        print(i)
