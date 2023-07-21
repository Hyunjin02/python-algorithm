import sys
input=sys.stdin.readline
dic={}
dic2={}
n,m=map(int,input().strip().split())

for i in range(n):
    insert=input().strip()
    dic[str(i+1)]=insert
    dic2[insert]=str(i+1)

for j in range(m):
    x=input().strip()
    if x in dic.keys():
        print(dic[x])
    elif x in dic2.keys():
        print(dic2[x])