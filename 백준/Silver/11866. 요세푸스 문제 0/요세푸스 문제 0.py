import sys

input = sys.stdin.readline
n,k=map(int,input().rstrip().split())
arr = []
result=[]
for i in range(n):
    arr.append(i+1)
i = k-1
while(True):
    if(len(arr)==0):
        break
    if(len(arr)-1<i):
        i=i-len(arr)
    else:
        result.append(arr.pop(i))
        i=i+k-1
print("<",end="")
print(*result,sep=", ",end="")
print(">")
