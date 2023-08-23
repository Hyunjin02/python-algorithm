import math

def isSosu(n):
    for i in range(2,int(math.sqrt(n))+1):
        if(n%i==0):
            flag=False
            return flag;
    return True

def sosu(a):
    if(a==0 or a==1 or a==2):
        return 2
    else:
        x=a
        while(True):
            if(isSosu(x)==True):
                return x
            else:
                x=x+1

n = int(input())
arr =[]
for i in range(n):
    arr.append(int(input()))

for i in range(n):
    print(sosu(arr[i]))