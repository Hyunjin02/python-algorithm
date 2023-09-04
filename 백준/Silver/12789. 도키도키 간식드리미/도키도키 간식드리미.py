import sys

input = sys.stdin.readline
n = int(input())
arr = list(map(int,input().split()))
stack=[]
s=1
i=0
flag = "Nice"
while(arr):
    if(arr[i]==s):
        arr.pop(i)
        s=s+1
    else:
        if(stack):
            if(stack[-1]==s):
                stack.pop(-1)
                s=s+1
            else:
                stack.append(arr.pop(i))
        else:
            stack.append(arr.pop(i))
while(stack):
    if(stack[-1]==s):
        stack.pop()
        s=s+1
    else:
        flag = "Sad"
        break
print(flag)


