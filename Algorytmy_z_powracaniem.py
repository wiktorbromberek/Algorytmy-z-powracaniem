import random

n=6

# x w procentach
def graf(n,x):
    l=[]
    m=[]
    count = 0
    k=x/100
    for i in range(n):
        m.append([0]*n)
    nasycenie = int((n*(n-1)*k)/2)
    # print(nasycenie)
    for i in range(n):
        l.append(i)
    random.shuffle(l)
    print(l)
    print()
    for i in range(len(l)-1):            
        m[l[i]][l[i+1]]+=1
        m[l[i+1]][l[i]]+=1
        count += 1
    m[l[-1]][l[0]]=1
    m[l[0]][l[-1]]=1
    count += 1
    while count<nasycenie:
        a=0;b=0;c=0
        while a==b or a==c or b==c or m[a][b]==1 or m[a][c]==1 or m[b][c]==1: 
            a,b,c = random.sample(range(0,n),3)
        m[a][b]=1; m[b][a]=1; m[a][c]=1; m[c][a]=1; m[b][c]=1; m[c][b]=1
        count += 3
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
        a=0;b=0;c=0
        while a==b or a==c or b==c or m[a][b]==1 or m[a][c]==1 or m[b][c]==1: 
            a,b,c = random.sample(range(0,n),3)
        m[a][b]=1; m[b][a]=1; m[a][c]=1; m[c][a]=1; m[b][c]=1; m[c][b]=1
        count += 3
    j = random.randrange(0,n)
    for i in range(n):
        m[j][i]=0
        m[i][j]=0
    return m

mm = graf(n,70)
for i in mm:
    print(i)

# print()
# m = graf_bez_cyklu(n,50)
# for i in m:
#     print(i)


O=[0]*n
path = []
visited=0
start=0

def hamilton(v,visited):
    O[v]=1
    visited+=1
    print(path)
    for i in range(n):
        if mm[v][i]==1:
            if i==start and visited==n:
                return True
            if O[i]==0:
                if hamilton(i,visited):
                    path.append(i)
                    return True
    O[v]=0
    visited -= 1
    return False

def hcycle():
    for i in range(n):
        path.append(0)
        start=0
        visited=0
        k=2
        hcycle = hamilton(start,visited)
        print(hcycle)
        # print(path)

hcycle()



