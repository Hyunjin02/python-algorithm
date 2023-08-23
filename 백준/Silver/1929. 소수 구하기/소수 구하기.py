import math

def isSosu(n):
    for i in range(2,int(math.sqrt(n))+1):
        if(n%i==0):
            flag=False
            return flag;
    return True

a,b = map(int,input().split())
for i in range(a,b+1):
    if(i==1):
        continue
    elif(isSosu(i)==True):
        print(i)
