import sys
n=[]
e=0
o=0
for i in range(1,len(sys.argv)):
    n.append(int(sys.argv[i]))
for i in n:
    if i%2==0:
        e=e+1
    else:
        o=o+1
print("even {} odd {}".format(e,o))
