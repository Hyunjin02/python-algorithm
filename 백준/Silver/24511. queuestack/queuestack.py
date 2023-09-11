import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
a = list(map(int,input().rstrip().split()))
b = list(map(int,input().rstrip().split()))
m = int(input())
c = list(map(int,input().rstrip().split()))
d=deque()
ans=[]
for i in range(n):
    if(a[i]==0):
        d.append(b[i])
for i in range(m):
    k=c[i]
    d.appendleft(k)
    ans.append(d.pop())

print(*ans)