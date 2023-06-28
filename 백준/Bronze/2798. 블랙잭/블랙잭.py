n,m=map(int,input().split())
a=list(map(int,input().split()))

y=max(a)

for i in range(0,n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            x=m-(a[i]+a[j]+a[k])
            if(x>=0 and x<=m-y):
                y=a[i]+a[j]+a[k]
print(y)