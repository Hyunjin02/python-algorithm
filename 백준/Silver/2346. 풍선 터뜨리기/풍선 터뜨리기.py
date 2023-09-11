import copy
import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
arr=deque(enumerate(map(int,input().rstrip().split())))
result=[]

while(arr):
    idx,number=arr.popleft()
    result.append(idx+1)
    if(number>0):
        arr.rotate(number*(-1)+1)
    if (number < 0):
        arr.rotate(number * (-1))

print(*result)