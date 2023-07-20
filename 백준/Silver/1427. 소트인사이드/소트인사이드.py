import sys
a=list(map(int,sys.stdin.readline().strip()))
a.sort(reverse=True)
b=''
for i in range(0,len(a)):
    b=b+str(a[i])
print(b)