a=int(input())
xList=[]
yList=[]
for i in range(0,a):
    x,y=map(int,input().split())
    if(a==1):
        print(0)
    else:
        xList.append(x)
        yList.append(y)
if(a!=1):
    print((max(xList)-min(xList))*(max(yList)-min(yList)))