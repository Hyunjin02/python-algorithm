n,b=map(int,input().split())
ans=''
while(n>=b):
    if(0<=n%b and n%b<=9):
        ans=ans+str(n%b)
    else:
        ans=ans+(chr(n%b+55))
    n=n//b

if(0<=n%b and n%b<=9):
    ans=ans+str(n)
else:
    ans=ans+(chr(n+55))

print(ans[::-1])