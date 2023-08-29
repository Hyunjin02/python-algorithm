import sys
input = sys.stdin.readline

arr = []
n=int(input().rstrip())
for i in range(n):
    order_input = input().split()
    order=int(order_input[0])
    if(len(order_input)>1):
        x=order_input[1]

    if(order==1):
        arr.append(x)

    elif(order==2):
        if(len(arr)>0):
            print(arr.pop())
        else:
            print(-1)

    elif(order==3):
        print(len(arr))

    elif(order==4):
        if(len(arr)==0):
            print(1)
        else:
            print(0)

    elif(order==5):
        if(len(arr)==0):
            print(-1)
        else:
            print(arr[len(arr)-1])
