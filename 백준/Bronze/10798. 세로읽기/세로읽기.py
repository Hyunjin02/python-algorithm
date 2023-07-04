a=[]
word=''
max=0
for i in range(0,5):
    a.append(list(input()))
    if(max<len(a[i])):
        max=len(a[i])

for i in range(0,max):
    for j in range(0,5):
        try:
            word=word+a[j][i]
        except:
            continue
print(word)