a,b=map(int,input().split())
c=[[0 for i in range(0,b)] for j in range(0,a)]
d=[[0 for i in range(0,b)] for j in range(0,a)]
e=[[0 for i in range(0,b)] for j in range(0,a)]

for i in range(0,a):
    c[i]=list(map(int,input().split()))
for i in range(0,a):
    d[i]=list(map(int,input().split()))
for i in range(0,a):
    for j in range(0,b):
        e[i][j]=c[i][j]+d[i][j]

for i in range(0,a):
    for j in range(0,b):
        print(e[i][j],end=' ')
    print()