a=[]
n,m=map(int,input().split())

def reverse(i,j):
    for k in range(0,(j-i+1)//2):
        temp = a[i+k]
        a[i+k]=a[j-k]
        a[j-k]=temp

for i in range(0,n):
    a.append(i+1)
for i in range(0,m):
    x,y=map(int,input().split())
    reverse(x-1,y-1)
for i in range(0,n):
    print(a[i],end=" ")