for i in range(int(input())):
    n,k=map(int,input().split())
    s=input()[:n]
    l=[i for i in s]
    #print(l)
    for i in range(len(l)):
        if l[i].isalpha():
            if l[i].islower():
                if ord(l[i])+k <= 122:
                    l[i]=chr(ord(l[i])+k)
                else:
                    q=(ord(l[i])+k)-122
                    while(q+96)>122:
                        q=(q+96)-122
                    l[i]=chr(96+q)
            if l[i].isupper():
                if ord(l[i])+k <= 90:
                    l[i]=chr(ord(l[i])+k)
                else:
                    q=(ord(l[i])+k)-90
                    l[i]=chr(64+q)
        '''if l[i].isdigit():
            if int(l[i])+k <=9:
                l[i]=str(int(l[i])+k)
            elif int(l[i])+k>9:
                l[i]=str(int(l[i])%9)'''


    print(''.join(l))
