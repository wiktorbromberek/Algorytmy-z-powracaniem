import random

n=10

def graf_30(n):
    l=[]
    m=[]
    for i in range(n):
        m.append([0]*n)
    nasycenie = (n*(n-1)*0.3)/2
    for i in range(n):
        l.append(i)
    random.shuffle(l)
    print(l)
    m[l[n-1]][l[0]]=1
    m[l[0]][l[-1]]=1
    for i in range(n-1):
        a = l[i]
        b = l[i+1]
        print(a,b)
        m[a][b]=1
        m[b][a]=1
    return m

matrix = graf_30(n)
for i in range(n):
    print(matrix[i])





