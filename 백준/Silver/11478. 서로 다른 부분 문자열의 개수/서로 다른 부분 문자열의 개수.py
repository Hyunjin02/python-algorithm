import sys
input=sys.stdin.readline

str = input().strip()
arr=set()

for i in range(len(str)):
    for j in range(i,len(str)):
        arr.add(str[i:j+1])
        
print(len(arr))
