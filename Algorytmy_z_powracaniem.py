import random

n=10

def graf(n,x):
    l=[]
    m=[]
    
    k=x/100
    for i in range(n):
        m.append([0]*n)
    nasycenie = int((n*(n-1)*k)/2)
    for i in range(n):
        l.append(i)
    random.shuffle(l)

    for i in range(len(l)-1):            
        m[l[i]][l[i+1]]+=1
        m[l[i+1]][l[i]]+=1
    print(l)
    print()
    for i in range(len(l)):
        print(m[i])

    for i in range(3):
        trojki=[]
        

    return nasycenie
print(graf(10,30)) 





