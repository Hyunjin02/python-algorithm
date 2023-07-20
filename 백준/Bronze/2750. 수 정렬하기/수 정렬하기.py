n=int(input())
list=[]
for i in range(n):
    list.append(int(input()))
#선택정렬
for i in range(n):
    min_index=i
    for j in range(i,n):
        if(list[min_index]>list[j]):
            min_index=j
    list[i],list[min_index] = list[min_index],list[i]

print(*list,sep='\n')