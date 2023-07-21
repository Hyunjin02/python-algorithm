import sys
input=sys.stdin.readline

n=int(input())
arr={}
for i in range(n):
    name,e_or_l=input().split()
    if(e_or_l=='enter'):
        arr[name]=e_or_l
    else:
        del arr[name]
arr=list(arr)
arr.sort(reverse=True)
print(*arr,sep='\n')