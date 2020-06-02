class node:
    def __init__(self,data=None):
        self.data=data
        self.next=None

class Linkedlist:
    def __init__(self):
        self.head=node()

    def append(self,data):
        new_node=node(data)
        cur=self.head
        while cur.next!=None:
            cur=cur.next
        cur.next=new_node

    def display(self):
        cur_node=self.head
        #print(self.head.next.data)
        while cur_node.next!=None:
            cur_node=cur_node.next
            print(cur_node.data,end=' ')

    def Sort(self):
        nn=self.head
        #print(self.head.data)
        while nn.next!=None:
            #print(nn.data)
            for i in range(n):
                nn=nn.next
                

b=Linkedlist()
n=int(input())
#l=list(map(int,input().split()))[:n]
for i in range(n):
    b.append(int(input()))

b.display()
b.Sort()
b.display()
