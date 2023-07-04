a=[]
for i in range(0,9):
    a.append(list(map(int,input().split())))
max=a[0][0]
max_i=0
max_j=0
for i in range(0,9):
    for j in range(0,9):
        if(a[i][j]>max):
            max=a[i][j]
            max_i=i
            max_j=j
print(max)
print(max_i+1,max_j+1)