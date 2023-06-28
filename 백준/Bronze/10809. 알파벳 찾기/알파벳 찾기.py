a=list(input())
charList= []
for i in range(ord('a'),ord('z')+1):
    charList.append(-1)

for i in range(len(a)):
    charList[ord(a[i])-ord('a')] = a.index(a[i])
print(*charList)

