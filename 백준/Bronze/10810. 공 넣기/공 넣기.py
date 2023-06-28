n,m=map(int,input().split())
a = []
for i in range(n):
    a.append(0)

for i in range(m):
    x,y,z=map(int,input().split())
    for j in range(x-1,y):
        a[j]=z
for i in range(n):
    print(a[i],end=" ")