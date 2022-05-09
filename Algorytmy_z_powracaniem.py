import random

n=100

# x w procentach
def graf(n,x):
    l=[]
    m=[]
    count = 0
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
        count += 1
    m[l[-1]][l[0]]=1
    m[l[0]][l[-1]]=1
    count += 1
    while count<nasycenie:
        if count+3>nasycenie:
            break
        a = random.randrange(0,n)
        b = random.randrange(0,n)
        while a==b or m[a][b]==1:
            b = random.randrange(0,n)
        c = random.randrange(0,n)
        while a==c or b==c or m[a][c]==1 or m[b][c]==1:
            c = random.randrange(0,n)
        m[a][b]=1; m[b][a]=1; m[a][c]=1; m[c][a]=1; m[b][c]=1; m[c][b]=1
        count += 3
    print()
    return m

def graf_bez_cyklu(n,x):
    l=[]
    m=[]
    count = 0
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
        count += 1
    m[l[-1]][l[0]]=1
    m[l[0]][l[-1]]=1
    count += 1
    while count<nasycenie:
        if count+3>nasycenie:
            break
        a = random.randrange(0,n)
        b = random.randrange(0,n)
        while a==b or m[a][b]==1:
            b = random.randrange(0,n)
        c = random.randrange(0,n)
        while a==c or b==c or m[a][c]==1 or m[b][c]==1:
            c = random.randrange(0,n)
        m[a][b]=1; m[b][a]=1; m[a][c]=1; m[c][a]=1; m[b][c]=1; m[c][b]=1
        count += 3
        # print(a,b,c)
    j = random.randrange(0,n)
    # print(j)
    for i in range(n):
        m[j][i]=0
        m[i][j]=0
    return m

mm = graf(n,50)
for i in mm:
    print(i)
