import math

n=int(input())

def ertostenes(limit):
    arr = [True]*(limit+1)
    arr[0]=False
    arr[1]=False
    for i in range(2,int(math.sqrt(limit))+1):
        for j in range(i*i,limit+1,i):
            arr[j]=False
    return arr

limits =1000000
arr_ = ertostenes(limits)

for i in range(n):
    x = int(input())
    count = 0
    for i in range(0,int(math.ceil(x/2))+1):
        if(arr_[i]==True and arr_[x-i]==True):
            count+=1
    print(count)
