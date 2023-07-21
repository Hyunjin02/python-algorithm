import sys
input = sys.stdin.readline

n=int(input())
arr=list(map(int,input().strip().split()))
m=int(input())
arr2=list(map(int,input().strip().split()))
arr3=set(arr)&set(arr2)

for i in arr2:
    if i in arr3:
        print(1, end=" ")
    else:
        print(0, end=" ")