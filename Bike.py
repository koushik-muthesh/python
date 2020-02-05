class Bike:
    def value(self,a):
        self.VIN=a[0]
        self.brand=a[1]
    def display(self):
        print("Vin:{} \n brand:{}".format(self.VIN,self.brand))
    def check(l1):
        q=l1[0]
        q1=l1[1]
        if q1[1]==q[1] and q[0]==q[0]:
            print("same")
        else:
            print("false")
l1=[]
for i in range(int(input())):
    obj=Bike()
    l=[]
    a=input().split(',')
    obj.value(a)
    obj.display()
    l.append(obj.VIN)
    l.append(obj.brand)
    l1.append(l)
print(l1)
Bike.check(l1)
    
              
              
