a,b,v=map(int,input().split())
n=v-a

if(n%(a-b)!=0):
    print(n//(a-b)+2)
else:
    print(n // (a - b) + 1)