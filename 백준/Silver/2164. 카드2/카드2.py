import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
que = deque()
for i in range(0,n):
    que.append(i+1)
while(len(que)>1):
    que.popleft()
    x=que.popleft()
    que.append(x)
print(que[0])