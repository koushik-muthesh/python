#import sys
#sys.setrecursionlimit(10**6)
def change():
    for i in range(1,len(l)-1):
        if l[i].count("X") == m:
            return False
        if i%2==0:
            l[i].insert(0,l[i].pop())
        else:
            l[i].append(l[i].pop(0))
    return True
 
 
def check(l,x,y,count):
    if x == n+1 and y == m-1:
        print(count)
        return True
    if x >= 0 and x < n+2 and y >= 0 and y < m and l[x][y] != "X":
        if change():
            if check(l,x+1,y,count+1) == True:
                return True
            if check(l,x,y+1,count+1) == True:
                return True
            #if count < m and check(l,x,y,count+1) == True:
                #return True
            return False
        else:
            return False
    return False
 
n,m = list(map(int,input().split()))
l = [] 
for i in range(n+2):
    l.append(list(input()))
#sol = [[0]*m for i in range(n+2)]
if check(l,0,0,0) == False:
    print("Impossible")
