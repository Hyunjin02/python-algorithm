a=list(map(int,input().split()))
b=[1,1,2,2,2,8]

for i in range(0,len(a)):
    a[i] = b[i]-a[i]
print(*a)