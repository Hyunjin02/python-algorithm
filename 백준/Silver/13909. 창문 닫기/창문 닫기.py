import math

n = int(input())
count=0
for i in range(1,int(math.sqrt(n))+1):
    if(i*i<=n):
        count+=1

print(count)