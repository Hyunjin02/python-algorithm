a= input().upper()
b=[]
c=[]

for i in range(0,len(a)):
    if(b.count(a[i])==0):
        b.append(a[i])
        c.append(a.count(a[i]))

max = max(c)
if(c.count(max)>1):
    print("?")
else:
    print(b[c.index(max)])