n=int(input())
count=0
for i in range(0,n):
    a=input()
    isGroup=True
    for j in range(0,len(a)-1):
        if(isGroup==True):
            for k in range(j+1,len(a)):
                #print(a[j],a[k],j,k)
                if(a[j]==a[k]):
                    if(a[k]==a[k-1]):
                        isGroup=True
                        #print('a[j]=',a[j],'a[k]=',a[k],'a[k-1]=',a[k-1])
                    else:
                        isGroup=False
                        break
    #print(a,isGroup)
    if(isGroup==True):
        count=count+1
print(count)