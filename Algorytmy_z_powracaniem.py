import random

n=10

def graf_30(n):
    l=[]
    m=[[0]*n]*n
    nasycenie = (n*(n-1)*0.3)/2
    for i in range(n):
        l.append(i)
    random.shuffle(l)

    for i in range(len(l)-1):            #
        m[][]=1
        m[][]=1
    print(l)
    for i in range(len(l)):
        print(m[i])

    return 
print(graf_30(n)) 





