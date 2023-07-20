import sys
n=int(sys.stdin.readline())
a= [0 for i in range(0,10001)]

for i in range(n):
    k=int(sys.stdin.readline())
    a[k]=a[k]+1

for i in range(0,10001):
    if(a[i]!=0):
        while(a[i]!=0):
            print(i)
            a[i]=a[i]-1