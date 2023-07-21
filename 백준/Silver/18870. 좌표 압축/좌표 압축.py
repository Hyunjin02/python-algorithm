import sys
input = sys.stdin.readline

n=int(input())
arr=list(map(int,input().strip().split()))
arr2=sorted(set(arr))

dic={}

for i in range(0,len(arr2)):
    dic[arr2[i]]=i

for i in range(0,len(arr)):
    print(dic[arr[i]],end=" ")