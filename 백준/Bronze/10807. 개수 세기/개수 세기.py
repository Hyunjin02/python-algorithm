a = int(input())
count=0
x=list(input().split())
b=int(input())
for i in range(a):
    if(int(x[i])==b):
        count+=1
print(count);