a,b=map(int,input().split())
c=[]
d=[]
for i in range(0,a):
    line=input()
    c.append(line)

for i in range(0,a-7):
    for j in range(0,b-7):
        start_b=0
        start_w=0
        for k in range(i,i+8):
            for l in range(j,j+8):
                if (k+l)%2==0:
                    if(c[k][l]!='W'):
                        start_b=start_b+1
                    if(c[k][l]!='B'):
                        start_w=start_w+1
                else:
                    if(c[k][l]!='W'):
                        start_w=start_w+1
                    if(c[k][l]!='B'):
                        start_b=start_b+1
        d.append(min(start_b,start_w))
print(min(d))

