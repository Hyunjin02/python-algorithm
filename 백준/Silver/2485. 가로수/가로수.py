def f_lcd(a,b):
    n1 = max(a,b)
    n2 = min(a,b)
    r=n1%n2
    while(r!=0):
        n1,n2=n2,r
        r=n1%n2
    return n2

n = int(input())
arr=[]
gap=[]
for i in range(n):
    arr.append(int(input()))

for i in range(n-1):
    gap.append(arr[i+1]-arr[i])
lcd=gap[0]

for i in range(len(gap)):
    lcd = f_lcd(lcd,gap[i])
count = 0

result = (arr[n-1]-arr[0])//lcd-n+1
print(result)

