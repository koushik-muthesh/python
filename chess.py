def attack(i,j,l):
    try:
        l[i+2][j+1].append(1)
        if(j-1)>=0:
            l[i+2][j-1].append(1)
        if(i-2)>=0:
            l[i-2][j+1].append(1)
        if(j-1)>=0 or (i-2)>=0:
            l[i-2][j-1].append(1)
        l[i+1][j+2].append(1)
        if(j-2)>=0:
            l[i+1][j-2].append(1)
        l[i-1][j+2].append(1)
        if(j-2)>=0 or (i-1)>=0:
            l[i-1][j-2].append(1)
    except Exception as e:
        p=1
    return l
            
class Chess:
    def __init__(self):
        self.l=[]
        for i in range(1,9):
            l1=[]
            q=97
            for j in range(8):
                l2=[]
                strs=chr(q)+''+str(i)
                l2.append(strs)
                l1.append(l2)
                q+=1
            self.l.append(l1)
        
    def match(self,a):
        for i in range(1,9):
            q=97
            for j in range(8):
                strs=chr(q)+''+str(i)
                if a==strs:
                    print(i,j)
                    self.l=attack(i-1,j,self.l)
                break
                        

            
    
    def display(self):
        self.l=[print(*i) for i in self.l]
        

if __name__=="__main__":
    a=input()
    obj=Chess()
    obj.match(a)
    obj.display()
