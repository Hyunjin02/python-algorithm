a = int(input())
s = ' '

for i in range(0,a):
    print(s*(a-i-1),end="")
    print('*'*(2*i+1))
for i in range(0,a):
    print(s*(i+1),end="")
    print('*'*((a-i-2)*2+1))