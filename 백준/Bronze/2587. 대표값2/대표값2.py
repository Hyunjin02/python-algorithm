list=[]
for i in range(5):
    list.append(int(input()))
avr=sum(list)//5
print(avr)

#삽입정렬
for i in range(1,5):
    for j in range(i,0,-1):
        if(list[j]<list[j-1]):
            list[j-1],list[j]=list[j],list[j-1]
        else:
            break
print(list[2])